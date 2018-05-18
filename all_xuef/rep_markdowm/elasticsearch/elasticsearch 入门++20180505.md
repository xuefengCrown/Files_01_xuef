## 简介

+ 基于Apache Lucene
+ Java编写，提供简单易用的RESTFul API
+ 轻松的横向扩展，可支持PB级的结构化或非结构化数据处理

## 使用场景

+ 海量数据分析引擎
+ 站内搜索引擎
+ 数据仓库

## 实际

+ 英国卫报-实时分析公众对文章的回应
+ 维基百科、github-站内实时搜索
+ 百度-实时日志分析平台

## 安装

### 单实例安装

```bash
> cd elasticsearch-5.5.0/bin
> elasticsearch
```



### java中操作elasticsearch

1. application.properties中添加配置

```properties
# es服务地址
spring.data.elasticsearch.cluster-nodes=47.97.197.165:9300
# 连接超时时间
spring.data.elasticsearch.properties.transport.tcp.connect_timeout=120s
```

2. 几个类

```java
文档 EsBlog
资源库 EsBlogRepository
控制器 BlogController (Client与Server通信的接口)
```

3. 数据保存到es与从es中检索数据

```java
save
检索 findBY...
```

4. 运行

```java
先启动es
运行java程序
```



## blog项目应用es实战

#### 自定义分析器（Analyzer）

<https://www.elastic.co/guide/en/elasticsearch/reference/5.5/analysis-custom-analyzer.html>

```http
// 必须在索引创建前进行设置
PUT my_index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_analyzer": { <!--分析器名-->
          "type":      "custom",
          "tokenizer": "standard",  <!--只能有一个-->
          "char_filter": [
            "html_strip"
          ],
          "filter": [
            "lowercase",
            "asciifolding"
          ]
        }
      }
    }
  }
}
```

```http
PUT my_index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_analyzer":
          "type":      "custom",
          "tokenizer": "standard",
          "char_filter": [
            "html_strip"
          ],
          "filter": [
            "lowercase",
            "asciifolding"
          ]
        }
      }
    }
  }
}
```



#### 建立索引和类型

```http
POST xblog/blog/1
{
  "title": "vim简明练级攻略",
  "summary": "很合理有节奏的vim使用指南",
  "content": 
}
```

#### 数据备份

<https://www.elastic.co/guide/en/elasticsearch/reference/5.5/modules-snapshots.html>



#### 中文分词器

<https://github.com/medcl/elasticsearch-analysis-ik>

**注意es版本与ik版本之间的一致性**

```bash

> wget https://github.com/medcl/elasticsearch-analysis-ik/archive/v5.5.0.tar.gz --no-check-certificate
> tar -zxvf v5.5.0.tar.gz
## 进入目录。执行mvn package  (用maven编译项目,生成target目录，编译、测试代码，生成测试报告，生成jar/war文件 )
> cd elasticsearch-analysis-ik-5.5.0/
> mvn package

> cd target
> cd releases/
> ls
elasticsearch-analysis-ik-5.5.0.zip
> unzip elasticsearch-analysis-ik-5.5.0.zip
> cd /home/xuef/es5/elasticsearch-5.5.0/plugins/ik
> cp -r /home/xuef/dev_tools/elasticsearch-analysis-ik-5.5.0/target/releases/* ./

至此，ik安装好了（如果你是集群，每个都需要按照此安装）

杀掉es，重启。
GET /_cat/plugins
d0KCJVU analysis-ik 5.5.0

```

#### 测试ik分词器

```http
http://47.97.197.165:9200/_analyze/?analyzer=ik_max_word&text=中华人民共和国国歌
```



#### 建立带分词器的索引和类型

```http
PUT xblog
{
  "settings" : {
        "analysis" : {
            "analyzer" : {
                "ik" : {
                    "tokenizer" : "ik_max_word"
                }
            }
        }
    },
    "mappings" : {
        "article" : {
            
            "properties" : {
                "title" : {
                    "type" : "text",
                    "analyzer" : "ik_max_word"
                },
                "summary" : {
                    "type" : "text",
                    "analyzer" : "ik_max_word"
                },
                "content" : {
                    "type" : "text",
                    "analyzer" : "ik_max_word"
                },
                "tags" : {
                    "type" : "text",
                    "analyzer" : "ik_max_word"
                }
            }
        }
    }
}
```



## http操作

```http
http://47.97.197.165:9200/_search?pretty

curl -XPOST 'http://47.97.197.165:9200/blog/articles/'
// PUT 必须指定具体的资源
curl -XPUT 'http://47.97.197.165:9200/blog/articles/12' 

http://47.97.197.165:9200/blog/blog/_search?pretty

http://47.97.197.165:9200/blog/blog/_search?q=username:xuef1991&pretty


```

## DSL 查询（参照官方文档）



## 批量操作



## 版本控制 （_version）











