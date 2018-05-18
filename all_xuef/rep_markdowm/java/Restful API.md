## 第一印象

**query** 

+ /user?name=tome **GET**

**detailInfo**

+ /user/1 **GET**

**create**

+ /user **POST**

**update**

+ /user/1 **PUT**

**delete**

+ /user/1 **DELETE**

---

## 简单说明

get请求的header有长度限制，所有创建和修改得使用post。

**Restful**

1. 用URL描述资源
2. 使用HTTP方法描述行为。使用HTTP状态码来表示不同的结果。
3. 使用json交互数据

---

## 编写第一个Restful API

### 编写针对RestfulAPI的测试用例



### 使用注解声明RestfulAPI



### 在RestfulAPI中传递参数

+ @RequestParam
+ SpringMVC 可以将参数组装进一个对象中去的
+ 传递分页参数 **Pageable**

### 其他

+ @PathVariable 映射url片段到参数
+ 在url中使用正则表达式来规范url

"/user/{id://d+}"

+ JSONView控制json输出内容



