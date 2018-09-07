

# 一个请求的处理流程

```java
DispatcherServlet
	doDispatch(HttpServletRequest request, HttpServletResponse response)
```



## ViewResolver

将数据解析成html？？？



## 静态资源



## 参数封装

### Converter（转换器）

String——>Integer



### Formatter（格式化器）

"2018-05-27"——>Date



# springboot中的springmvc

```java
WebMvcAutoConfiguration
```

## 自动配置

https://docs.spring.io/spring-boot/docs/1.5.10.RELEASE/reference/htmlsingle/#boot-features-developing-web-applications



# 5、如何修改SpringBoot的默认配置

模式：
1）、SpringBoot在自动配置很多组件的时候，先看容器中有没有用户自己配置的（@Bean、@Component）如
果有就用用户配置的，如果没有，才自动配置；如果有些组件可以有多个（ViewResolver）将用户配置的和自己默认的组合起来；
2）、在SpringBoot中会有非常多的xxxConfigurer帮助我们进行扩展配置
3）、在SpringBoot中会有很多的xxxCustomizer帮助我们进行定制配置



# 6. 扩展SpringMVC

## 添加配置

```java
// 使用WebMvcConfigurerAdapter可以来扩展SpringMVC的功能
@Configuration
public class MyMvcConfig extends WebMvcConfigurerAdapter{
  	@Override
    public void addViewControllers(ViewControllerRegistry registry) {
       // super.addViewControllers(registry);
        //浏览器发送 /register 请求,来到 register.html 页面
        registry.addViewController("/register").setViewName("register");
    }
} 
```



## interceptor（拦截器）



## view controller



