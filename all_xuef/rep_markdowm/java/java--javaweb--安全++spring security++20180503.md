## 如何进阶

把一个知识点所有常见场景和特性都覆盖到

不止讲自己写的代码，还要讲框架的源码

不止要实现功能，还要封装起来能重用，能给别人用。

### 认证和授权

同时支持多种认证方式

同时支持多种前端渠道

支持集群环境，跨应用工作，session控制，控制用户权限，防护与身份认证相关的攻击。

### 目标

实现一个可重用的，企业级的认证和授权模块。

+ 深入理解Spring Sec及相关框架的原理、功能和代码
+ 可以基于 SS及相关框架独立开发认证授权相关功能
+ 掌握抽象和封装的常见技巧，可以编写可重用的模块供他人使用




## Spring Security 能做什么？

1. 认证（你是谁）
2. 授权（你能组什么）
3. 攻击防护（防止伪造身份）

## SS 基本原理

## 自定义用户认证逻辑

1. 处理用户信息获取逻辑 UserDetailsService


```java
public interface UserDetailsService {
    UserDetails loadUserByUsername(String var1) throws UsernameNotFoundException;
}
  实现UserDetailsService接口，重写loadUserByUsername方法。ss会调用这个方法（当然你得把实现类交给spring容器来管理，以保证ss在需要调用的时候能找到），loadUserByUsername会返回一个封装了用户名、密码以及权限信息，还有密码是否过期等信息的UserDetails对象。参见UserDetails接口：
  public interface UserDetails extends Serializable {
    Collection<? extends GrantedAuthority> getAuthorities();
    String getPassword();
    String getUsername();
    boolean isAccountNonExpired();
    boolean isAccountNonLocked();
    boolean isCredentialsNonExpired();
    boolean isEnabled();
  }
  ss会拿着这些信息（来自内存或者来自数据库）与client端传过来的账号密码进行比对。
  一般情况下，当注册密码时，我们需要对原始密码进行加密。
  我们知道，加密密码时，我们的加密器都是自动注入到IOC容器的。如下
  @Autowired
  private PasswordEncoder passwordEncoder;
  那么，加密器来自于哪儿呢？
  我们需要在配置类中（BrowserSecurityConfig extends WebSecurityConfigurerAdapter）配置一个加密器。
  @Bean
  public PasswordEncoder passwordEncoder(){
  	return new BCryptPasswordEncoder();
  }
  一旦你把加密器交给spring，ss就能在适当时候使用该加密器（如加密从client拿到的原始密码，然后与userdetails中的密码比对）。
```



2. 处理用户校验逻辑 UserDetails
3. 处理密码加密解密 PasswordEncoder

## 个性化用户认证流程

1. 自定义登录页面

   ```java
   @Override
   	protected void configure(HttpSecurity http) throws Exception {
   		// 都可以访问
   		http
               .authorizeRequests()
                   .antMatchers("/css/**", "/js/**", "/fonts/**", "/index").permitAll()
                   .antMatchers("/admins/**").hasRole("ADMIN")
   				// 登录用户才可以新增博客
   				.antMatchers("/space/*/blogs/edit").hasRole("USER")
                   .and()
               .formLogin()
             		// 指定登录页,此处指定/authentication/require 来处理登录
                   .loginPage("/authentication/require").permitAll()
             		// 告诉UsernamePasswordAuthenticationFilter 处理/authentication/form （POST）
             		// 这个请求。默认是处理 /login （POST）
             		.loginProcessingUrl("/authentication/form")
   				// 登录失败后处理的url
                   .failureUrl("/login-error")
    				// 登录成功后调用
                   .successHandler(blogAuthenticationSucHandler)
                   //.failureHandler(blogAuthenticationFailureHandler)
   				.and()
   			.csrf().disable(); // 关闭spring security 的防止跨站攻击
   	}
   ```

   ​

2. 自定义登录成功处理（每日登录奖励）

ss 默认的登录成功处理是，跳到引发登录的请求上。

**自定义**

实现接口: AuthenticationSuccessHandler

3. 自定义登录失败处理（密码输入次数记录）

### 通用登录后处理模块

1. 支持同步登录和异步登录



## 可重用的安全模块（security core）

1. loginPage 可以在 applications.properties 中配置
2. Restful 风格的响应应该是状态码和json数据



## 认证流程源码级详解

### 1. 认证处理流程

**过滤器链**

--->未认证

UsernamePasswordAuthenticationFilter （attemptAuthentication）

AuthenticationManager

AuthenticationProvider

UserDetailService

UserDetails

--->Authentication（已认证）

### 2. 认证结果如何在多个请求之间共享

请求过来，查看session，如果对象在，就取出来放在线程中。

返回时，查看线程中有认证信息对象，如果有就取出来放在session中。

多线程，保证安全。

### 3. 如何获取用户认证信息

```java
@GetMapping("/authinfo")
public Object getCurrentUser(){ // or (Authentication auth)
  return SecurityContextHolder.getContext().getAuthentication();
}
```

### 4. 基于用户角色的登陆后跳转

```
在onAuthenticationSuccess中调用父类的登录认证成功后跳转方法。
需要在SecurityConfig 中添加 antMatchers
```

## 攻防

### CSRF（跨站请求伪造防护）