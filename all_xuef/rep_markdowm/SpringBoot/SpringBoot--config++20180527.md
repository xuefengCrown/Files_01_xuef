## 模式

```java
xxxAutoConfiguration   // 自动配置类
//每一个这样的 xxxAutoConfiguration类都是容器中的一个组件，都加入到容器中；用他们来做自动配置；

```

Ctrl + N 搜索

4）、以HttpEncodingAutoConfiguration（Http编码自动配置）为例解释自动配置原理；

```java
@Configuration   //表示这是一个配置类，以前编写的配置文件一样，也可以给容器中添加组件
@EnableConfigurationProperties(HttpEncodingProperties.class)  //启动指定类的
ConfigurationProperties功能；将配置文件中对应的值和HttpEncodingProperties绑定起来；并把
HttpEncodingProperties加入到ioc容器中
@ConditionalOnWebApplication //Spring底层@Conditional注解（Spring注解版），根据不同的条件，如果
满足指定的条件，整个配置类里面的配置就会生效；    判断当前应用是否是web应用，如果是，当前配置类生效
@ConditionalOnClass(CharacterEncodingFilter.class)  //判断当前项目有没有这个类
CharacterEncodingFilter；SpringMVC中进行乱码解决的过滤器；
@ConditionalOnProperty(prefix = "spring.http.encoding", value = "enabled", matchIfMissing =
true)  //判断配置文件中是否存在某个配置  spring.http.encoding.enabled；如果不存在，判断也是成立的
//即使我们配置文件中不配置pring.http.encoding.enabled=true，也是默认生效的；
public class HttpEncodingAutoConfiguration {
 
   //他已经和SpringBoot的配置文件映射了  
   private final HttpEncodingProperties properties;
  //只有一个有参构造器的情况下，参数的值就会从容器中拿
   public HttpEncodingAutoConfiguration(HttpEncodingProperties properties) {  
    this.properties = properties;        
   }    
 
    @Bean   //给容器中添加一个组件，这个组件的某些值需要从properties中获取
    @ConditionalOnMissingBean(CharacterEncodingFilter.class) //判断容器没有这个组件？    
    public CharacterEncodingFilter characterEncodingFilter() {    
      CharacterEncodingFilter filter = new OrderedCharacterEncodingFilter();        
      filter.setEncoding(this.properties.getCharset().name());        
      filter.setForceRequestEncoding(this.properties.shouldForce(Type.REQUEST));        
      filter.setForceResponseEncoding(this.properties.shouldForce(Type.RESPONSE));        
      return filter;        
    } 
```

根据当前不同的条件判断，决定这个配置类是否生效？
一但这个配置类生效；这个配置类就会给容器中添加各种组件；这些组件的属性是从对应的properties类中获取
的，这些类里面的每一个属性又是和配置文件绑定的；
5）、所有在配置文件中能配置的属性都是在xxxxProperties类中封装者‘；配置文件能配置什么就可以参照某个功
能对应的这个属性类

```java
@ConfigurationProperties(prefix = "spring.http.encoding")  
//从配置文件中获取指定的值和bean的属性进行绑定
public class HttpEncodingProperties {
   public static final Charset DEFAULT_CHARSET = Charset.forName("UTF‐8");
```



精髓：
1）、SpringBoot启动会加载大量的自动配置类
2）、我们看我们需要的功能有没有SpringBoot默认写好的自动配置类；
3）、我们再来看这个自动配置类中到底配置了哪些组件；（只要我们要用的组件有，我们就不需要再来配置了）
4）、给容器中自动配置类添加组件的时候，会从properties类中获取某些属性。我们就可以在配置文件中指定这
些属性的值；
xxxxAutoConfigurartion：自动配置类；给容器中添加组件

xxxxProperties:封装配置文件中相关属性；

