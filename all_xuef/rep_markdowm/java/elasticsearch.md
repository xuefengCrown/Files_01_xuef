# Install

## 阿里云服务器下安装elasticSearch

1. env

```
centos 7.5
jdk1.8.0_121以上版本
elasticsearch 5

```

2. 配置

```bash
注意请不要使用root来运行。使用普通账号

运行时可能会报以下错误
max file descriptors [4096] for elasticsearch process likely too low, increase to at least [65536]
max number of threads [1024] for user [lishang] likely too low, increase to at least [2048]

我们需要去修改 /etc/security/limits.conf 这个文件
在末尾增加
xuef soft nofile 65536
xuef hard nofile 65536
xuef soft nproc 2048

max virtual memory areas vm.max_map_count [65530] likely too low, increase to at least [262144]
这时需要去修改 /etc/sysctl.conf 
添加
vm.max_map_count= 262144
并执行命令：
sysctl -p

来到config文件夹打开 jvm.options 这个文件
-Xms1g

vim elasticsearch.yml
network.host: 0.0.0.0
http.port: 9200  //默认端口
cluster.name: jtthink-search

# 防火墙放行 9200
iptables -I INPUT -p tcp --dport 9200 -j ACCEPT
# 或者关闭防火墙

# 另外，阿里云服务器中药添加安全组规则，放行9200
```



## 一些坑

```xml
vim elasticsearch.yml
# : 后必须有空格
cluster.name: xblog-search

```

# 基本用法

```http
// 创建 blog 索引
PUT /blog?pretty
// 查看
GET /_cat/indices?v


Relational DB -> Databases -> Tables -> Rows -> Columns
Elasticsearch -> Indices -> Types -> Documents -> Fields


```

## 重启kibana

```bash
fuser -n tcp 5601
kill ...
```

