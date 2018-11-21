#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

// linux cp command
int main(int argc, char *argv[]){

  int fd_src, fd_dest;
  char buf[1024];
  if(argc < 3){
    printf("./mycp src_name dest_name\n");
    exit(1);
  }

  fd_src = open(argv[1], O_RDONLY);
  fd_dest = open(argv[2], O_CREAT | O_WRONLY | O_EXCL, 0644);

  int len = 0;
  while((len = read(fd_src, buf, sizeof(buf))) > 0 ){
    write(fd_dest, buf, len);
  }
  close(fd_src);
  close(fd_dest);

  return 0;
}
