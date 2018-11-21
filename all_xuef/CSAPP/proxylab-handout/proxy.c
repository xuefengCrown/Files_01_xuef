#include <stdio.h>
/*
	a web proxy
*/
#include "csapp.h"

void doit(int fd);
void read_requesthdrs(rio_t *rp);
int parse_uri(char *uri, char *filename, char *cgiargs);
void serve_static(int fd, char *filename, int filesize);
void get_filetype(char *filename, char *filetype);
void serve_dynamic(int fd, char *filename, char *cgiargs);
void clienterror(int fd, char *cause, char *errnum, 
		 char *shortmsg, char *longmsg);
		 
/* Recommended max cache and object sizes */
#define MAX_CACHE_SIZE 1049000
#define MAX_OBJECT_SIZE 102400

/* You won't lose style points for including this long line in your code */
static const char *user_agent_hdr = "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:10.0.3) Gecko/20120305 Firefox/10.0.3\r\n";

int main()
{
    int listenfd; // 监听描述符 
    int *connfd; // 已连接描述符
    char hostname[MAXLINE], port[MAXLINE];
    socklen_t clientlen;
    struct sockaddr_storage clientaddr;
	
	/* Check command line args */
    if (argc != 2) {
		fprintf(stderr, "usage: %s <port>\n", argv[0]);
		exit(1);
	}
	
	// 服务器创建一个监听描述符, 准备接收连接请求。
    listenfd = Open_listenfd(argv[1]);
	pthread_t tid;
    while (1) {
		clientlen = sizeof(clientaddr);
		connfd = Malloc(sizeof(int));
		*connfd = Accept(listenfd, (SA *)&clientaddr, &clientlen); //line:netp:tiny:accept
		
		Getnameinfo((SA *) &clientaddr, clientlen, hostname, MAXLINE, 
						port, MAXLINE, 0);
		printf("Accepted connection from (%s, %s)\n", hostname, port);
		// 处理一个 HTTP 事务
		//doit(connfd);
		//Close(connfd);
		Pthread_create(&tid, NULL, thread, connfd);
    }
    //printf("%s", user_agent_hdr);
}

void *thread(void *vargp){
	int connfd = *((int *) vargp);
	Pthread_detach(pthread_self());
	Free(vargp);
	doit(connfd);
	Close(connfd);
	return NULL;
}

/*
代理和web服务器的异同是什么：
1. 都需要接收客户端发送来的HTTP请求；都需要解析HTTP请求行。代理解析请求行时，
需要得到服务器的ip、端口和资源路径（为了连接服务器和构造请求报头），而不需要关注是动态和静态内容。

2. 我们还需要构造一些固定的请求报头，组成完整的HTTP请求发给服务器。
让proxy充当客户端将信息转发给正确的服务器
3. 要接收服务器发回的信息，然后发给客户端。

*/
void doit(int fd){
	char buf[MAXLINE];
	rio_t rio; // 缓冲区
	
	//将描述符 fd和 rio处的一个类型为 rio_t的缓冲区联系起来
	Rio_readinitb(&rio, fd);
	
	// 读取一行
	if (!Rio_readlineb(&rio, buf, MAXLINE))  //line:netp:doit:read request
        return;
    printf("Request Headers: %s.\n", buf);
	
	char method[MAXLINE], uri[MAXLINE], version[MAXLINE]
	// GET /hub/index.html HTTP/1.0
	sscanf(buf, "%s %s %s", method, uri, version);
	if (strcasecmp(method, "GET")) {
        clienterror(fd, method, "501", "Not Implemented", "Tiny does not implement this method");
        return;
    }
	
	/* Parse URI from GET request */
	// 解析请求行时，需要得到服务器的ip、端口和资源路径（为了连接服务器和构造请求报头）
	char hostname[MAXLINE], path[MAXLINE], port[MAXLINE];
    parse_uri(uri, hostname, path, port);
	
	/* Build the request header*/
	char request_header[MAXLINE];
    build_request_header(request_header, hostname, path, port, &rio);

    /*Connect to server*/
	int serverfd;
    serverfd = Open_clientfd(hostname, port);
    if(serverfd<0){
        printf("connection failed\n");
        return;
    }
	
    /*Write the http header to server*/
	rio_t server_rio;
    Rio_readinitb(&server_rio, serverfd);
    Rio_writen(serverfd, request_header, strlen(request_header));

    /*receive message from end server and send to the client*/
    size_t n;
    while( (n=Rio_readlineb(&server_rio,buf,MAXLINE))!=0 )
    {
        printf("proxy received %zu bytes,then send\n",n);
        Rio_writen(fd, buf, n);
    }
    Close(serverfd);
}

/* parse the uri to get hostname,file path ,port */
void parse_uri(char *uri, char *hostname, char *path, int *port)
{
	// 需要判断地址里有没有带端口
    *port = 80;
    char *pos = strstr(uri,"//");

    pos = (pos != NULL? pos+2:uri);

    char *pos2 = strstr(pos,":");
    if(pos2 != NULL) {
        *pos2 = '\0';
        sscanf(pos, "%s", hostname);
        sscanf(pos2+1, "%d%s", port, path);
    } else {
        pos2 = strstr(pos,"/");
        if(pos2 == NULL)
        {
            sscanf(pos, "%s", hostname);
        }else {
			*pos2 = '\0';
            sscanf(pos, "%s", hostname);
            *pos2 = '/';
            sscanf(pos2, "%s", path);
        }
    }
    return;
}
/*
构建新的请求头
需要将请求头中 Host、User-Agent、Connection、Proxy-Connection等 key的 value部分修改为指定的信息，并且其他请求头不变
*/
void build_request_header(char *proxy_req_header, char *hostname, char *path, int port, rio_t *rio){
	char request_line[MAXLINE]; // 请求行
	sprintf(request_line, "GET %s HTTP/1.0\r\n", path);
	
	char buf[MAXLINE], host_header[MAXLINE], other_header[MAXLINE];
	while(Rio_readlineb(rio, buf, MAXLINE) > 0){
		if(!strcmp(buf, "\r\n") break;
		if(!strncasecmp(buf,"host",strlen("host")))/*Host:*/
        {
            strcpy(host_header,buf);
		}else if(strncasecmp("Connection", buf, strlen("Connection")) 
            && strncasecmp("Proxy-Connection", buf, strlen("Proxy-Connection"))
            && strncasecmp("User-Agent", buf, strlen("User-Agent"))){
			strcat(other_header, buf);
		}
	}
	sprintf(proxy_req_header,"%s%s%s%s%s%s%s",
            request_line,
            host_header,
            "Connection: close",
            "Proxy-Connection: close",
            user_agent_hdr,
            other_header,
            "\r\n");
	printf("proxy_req_header:\n", proxy_req_header);
    return ;
}

/*
 * clienterror - returns an error message to the client
 */
void clienterror(int fd, char *cause, char *errnum, 
         char *shortmsg, char *longmsg) 
{
    char buf[MAXLINE], body[MAXBUF];

    /* Build the HTTP response body */
    sprintf(body, "<html><title>Tiny Error</title>");
    sprintf(body, "%s<body bgcolor=""ffffff"">\r\n", body);
    sprintf(body, "%s%s: %s\r\n", body, errnum, shortmsg);
    sprintf(body, "%s<p>%s: %s\r\n", body, longmsg, cause);
    sprintf(body, "%s<hr><em>The Tiny Web server</em>\r\n", body);

    /* Print the HTTP response */
    sprintf(buf, "HTTP/1.0 %s %s\r\n", errnum, shortmsg);
    Rio_writen(fd, buf, strlen(buf));
    sprintf(buf, "Content-type: text/html\r\n");
    Rio_writen(fd, buf, strlen(buf));
    sprintf(buf, "Content-length: %d\r\n\r\n", (int)strlen(body));
    Rio_writen(fd, buf, strlen(buf));
    Rio_writen(fd, body, strlen(body));
}
