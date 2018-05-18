当spring整合各种框架时，添加的各种配置不过是利用spring容器生成了一些特定对象，而这些对象对各自框架进行了初始化和管理。

# 容器

@Configuration声明为配置类

@Bean给容器中注册组件

@ComponentScan-自动扫描组件&指定扫描规则

@Scope 指定对象是否单例

​	单实例，默认容器启动时就创建对象。

```java
@Configuration
public class MyConfig{
  
  @Scope("prototype")
  @Bean
  public Person person(){
    
    return new Person("rose",23);
  }
}
```



# 扩展原理



# web

