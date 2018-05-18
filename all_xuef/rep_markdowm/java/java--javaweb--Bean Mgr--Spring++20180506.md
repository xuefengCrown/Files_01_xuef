

# 手动开启Spring

```java
// 当然，直接参考官方文档就好
ApplicationContext ctx = new ClassPathXmlApplicationContext("applicationContext.xml");
/**
会读取xxx.xml配置文件，生成配置的bean.
如果是功能性的bean，如JPA的EntityManagerFactory，则该对象会扫描@Entity类，
为其在数据库中生成对应的表。
当然，一般的bean对象也可以做些事情，这在《架构探险：从零开始写 JavaWeb 框架》中可见。
类的静态代码块中代码会执行 static{}
构造器会被调用。我们可以在静态代码块和构造方法中添加自己需要的动作，是需要而定。
区别在于，static{}中代码只在类加载时执行一次。

《Java编程思想》需要认真读。
它几乎告诉你一切细节。
当然，你还需要去阅读框架的源码，才能对《Java编程思想》中所说的东西有所理解。
*/
```



# Spring 源码解读与设计分析

## IOC根容器 BeanFactory

BeanFactory 是个接口，定义了一套所有的IOC容器都要遵循的规范。

ApplicationContext

WebApplicationContext



## DefaultListableBeanFactory

spring如何载入和装配资源

XmlBeanDefinitionReader 负责读取Bean 定义

将各种资源统一映射为Resource

+ ClassPathResource
+ FileSystemResource



