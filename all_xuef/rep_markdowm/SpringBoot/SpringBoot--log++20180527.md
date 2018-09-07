# 框架介绍

slf4j 是日志门面（面向这个接口编程）

log4j （slf4j的具体实现之一，存在一些问题）

logback（更好的实现）



# 我们能做什么？

我们能控制日志的输出位置，输出级别和输出格式。

## 输出级别

```java
//记录器    
Logger logger = LoggerFactory.getLogger(getClass());    
@Test    
public void contextLoads() {    
  //System.out.println();  千万别这么写      
  //日志的级别；        
  //由低到高   trace<debug<info<warn<error        
  //可以调整输出的日志级别；日志就只会在这个级别以以后的高级别生效        
  logger.trace("这是trace日志...");        
  logger.debug("这是debug日志...");        
  //SpringBoot默认给我们使用的是info级别的，没有指定级别的就用SpringBoot默认规定的级别；root级别

  logger.info("这是info日志...");        
  logger.warn("这是warn日志...");        
  logger.error("这是error日志...");        
}
```

## 输出格式

```xml
<!--
  日志输出格式：
    %d表示日期时间，        
    %thread表示线程名，        
    %‐5level：级别从左显示5个字符宽度        
    %logger{50} 表示logger名字最长50个字符，否则按照句点分割。         
    %msg：日志消息，        
    %n是换行符        
    ‐‐>
    %d{yyyy‐MM‐dd HH:mm:ss.SSS} [%thread] %‐5level %logger{50} ‐ %msg%n
```

## 在springboot中配置

```properties
logging.level.com.atguigu=trace
#logging.path=
# 不指定路径在当前项目下生成springboot.log日志
# 可以指定完整的路径；
#logging.file=G:/springboot.log
# 在当前磁盘的根路径下创建spring文件夹和里面的log文件夹；使用 spring.log 作为默认文件
logging.path=/spring/log
#  在控制台输出的日志的格式
logging.pattern.console=%d{yyyy‐MM‐dd} [%thread] %‐5level %logger{50} ‐ %msg%n
# 指定文件中日志输出的格式
logging.pattern.file=%d{yyyy‐MM‐dd} === [%thread] === %‐5level === %logger{50} ==== %msg%n
```

## springboot的默认配置

```java
spring-boot-1.5.14.RELEASE.jar
	org.springframework.boot.logging
		LoggingApplicationListener
		LoggingSystemProperties
		
  		logback
          base.xml
          defauts.xml
```



## 高级配置

异步日志

自动归档

​		

