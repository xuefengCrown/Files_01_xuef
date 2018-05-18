# controller

## 路径映射

@RequestMapping(value={"/", "/index"})

1. 可以放在类上
2. 可以放在方法上
3. @GetMapping、@PostMapping、@DeleteMapping



## 参数获取

**（spring系列为我们做了很多解析工作）**

web应用重要的工作：请求个数据解析，通信

```http
https://www.nowcoder.com/discuss/73723?type=0&order=0&pos=1&page=2
```

### @PathVariable

获取/profile/{groupId}/{userId}/的groupId与userId

request.getPathInfo()

### @RequestParam

获取?后的参数，如 type、order、pos、page

可以设置默认值defaultValue

request.getQueryString()

## 携带数据

## @Request



## @Session



## @Model

## 重定向

### RedirectView

1. 301 永久转移
2. 302 临时

### redirect 重定向

302

```java
return "redirect:/"
```

### 错误处理

```java
@ExceptionHandler
@ResponseBody
public String error(Exception e){
  return "error: " + e.getMessage();
}
```



# IOC



# AOP

**Spring框架的很多方面都是编程的典范，比如AOP的实现，值得认真学习的极优秀范例**

## 打log

在阿里，所有的服务都要做日志记录，打log。

你不可能在所有的方法内部都写上logger.info("...");

### 统计每个页面的运行情况

1. 打开多少次
2. 每次请求的时间，打开的时间，页面加载耗时是多少

```java
@Aspect
@Component
public class LogAspect{
  private static final Logger logger = LoggerFactory.getLogger(LogAspect.class);
  
  @Before("execution(* com.xuef.blog.controller.*Controller.*(..))")
  public void beforeMethod(JoinPoint joinPoint){}
  
  @After()
  @After("execution(* com.xuef.blog.controller.*Controller.*(..))")
  public void afterMethod(JoinPoint joinPoint){
    
  }
}
```



## 权限管理



## 其他通用（统一）服务





# HTTP协议

《HTTP权威指南》



# 模板引擎

## thymeleaf



## Velocity

