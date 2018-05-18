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

1. 处理用户信息获取逻辑 UserDetailService
2. 处理用户校验逻辑 UserDetails
3. 处理密码加密解密 PasswordEncoder


## 个性化用户认证流程

1. 自定义登录页面
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