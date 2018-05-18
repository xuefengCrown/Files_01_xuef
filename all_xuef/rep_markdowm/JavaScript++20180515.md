# 数据类型

## 基本类型

number

string

null

undefined

## 引用类型

### object

{}、[]、/^$/、Date

### function









# 预解释（变量提前声明）

在当前的作用域中，js代码执行前，浏览器首先会默认的把所有带var和function的进行提前的声明和定义。

var 会进行声明；

function 既声明又定义；

刚开始，只对全局作用域进行预解释。函数中的变量只有当函数执行才会存在。

函数定义，只是代码以字符串形式被存储在堆内存中。



预解释时，if中的var也预解释。

## 声明（declare）

var num；

## 定义（defined）

num=12；



# 自执行函数（定义与执行一起完成）

```javascript
(function(num){
  
})();
~function(){}();
```



# 内存

## 栈内存

提供供js代码执行的环境（作用域：全局和私有）（如全局作用域就是个栈内存）

## 堆内存

用来存储引用数据类型的值

对象存储的是属性名和值

代码存储的是代码字符串



# js 内存释放

《高程3》

1. 堆内存

只要被引用，就不会被销毁。（取消引用，obj = null;）

2. 栈内存

一般，函数执行会形成一个新的私有作用域，当私有作用域中的代码执行完成后，栈内存销毁。

但，如果当前私有作用域中的部分内存被作用域以外的东西占用了，那么当前这个作用域就不会销毁了。

# 作用域链

## 函数执行过程

1. 当函数执行时，首先会开辟一个新的私有作用域
2. 如果有形参，先给形参赋值
3. 进行私有作用域中的预解释
4. 代码从上到下执行

函数形成一个私有的作用域，保护里面的变量不受外界干扰。（当然也不干扰外界）

## 变量作用域

1. 函数中的形参，声明的变量是私有变量。与外界无关
2. 函数中变量如果不是私有的，则往上级作用域中查找

## 如何查找上级作用域

当前函数是在哪个作用域下定义的，那么它的上级作用域就是谁。

和函数在哪执行的，没有关系。

# in

if ("name" in person)



# return

```javascript
function f1(){
  return function(){
    
  };
  console.log("不会执行");
}
```



# this

js中的this代表的是当前行为执行的主体

js中的context代表的是当前行为执行的环境（区域）

this是谁和函数在哪定义和在哪执行的没有关系

1. 函数执行，首先看前面有没有“.”，有的话，前面就是this，否则就是this就是Window。
2. 自执行函数中的this永远是 window。
3. 给元素的某一个事件绑定方法，当事件触发的时候，执行对应的方法，方法中的this是当前的元素。



# DOM

通过dom方法获取的元素或者元素集合都是对象类型，也存在一块堆内存，里面存着该元素的各种属性和方法。









# 面向对象

## 单例模式

```javascript
// 单例模式中，我们也把person1 叫做模式空间
var person1 = {
  name: "rose",
  age: 20
};
```

### 单例模式与简单的模块化开发

根据当前项目的需求划分成几个功能版块，每个人负责一部分，同时开发，最后把每个人的代码进行合并。

百度首页

1. 搜索
2. 页卡
3. 登录
4. 换肤

```javascript
var tabRender = {
  change: function(){
    
  },
  ...
};
```

公共组件由技术好点的来写（general.js   util.js）



## 构造函数模式



## 工厂模式

单例模式属于手工作业模式。不能批量生产

```javascript
var personFactory = function(name, age){
  var obj;
  obj.name = name;
  obj.age = age;
  obj.eat = function(){
    console.log(this.name + "eat");
  };
  return obj;
};
```





## 原型链模式

```javascript
function Person(name, age){
  this.name = name;
  this.age = age;
}
Person.prototype.eat = function(){
  console.log(this.name + "eat");
};

var p1 = new Person("jack", 20);
var p2 = new Person("rose", 19);
p1.eat === p2.eat // true
```

1. 每一个函数类型（普通函数，类）都有一个天生属性：prototype（原型），并且这个属性是一个对象类型的值。
2. 在prototype上，浏览器给它加了一个属性constructor（构造函数），属性值是当前函数（类）本身。
3. 每一个对象数据类型（普通对象，实例，prototype）也天生自带一个属性 \_\_proto\__，属性值是当前实例所属类的原型（prototype） 



```javascript
dir(Array.prototype)
dir(Object.prototype)

p1.hasOwnProperty("x");
// f1的私有属性上没有这个方法，那如何处理的呢？
通过对象名.属性名 的方式获取属性值的时候，首先在对象的私有属性上进行查找，如果存在，则使用这个私有属性。
如果没有，则通过__proto__找到所属类的原型，原型上存在的话，获取的是公有的属性值。
```

把window、document、div、a 的原型链一级一级的结构画出来。

# Function

函数类（所有的函数都是它的实例）

记住： 所有的类都是函数

## 函数的多重角色

1. 普通函数

执行的时候形成私有的作用域。

2. 类

可以有自己的实例，也有一个叫 prototype 属性是自己的原型，它的实例都可以指向自己的原型。

3. 普通对象

作为对象可以有自己的私有的属性，可以通过\__proto__ 找到 Function.prototype

jQuery 就重复利用了函数的三种角色。



# 关键函数

## call

Function.prototype.call // 改变this 指向

```javascript
fn.call(obj);
// 执行call，让fn方法中的this变为第一个参数值 obj，然后再把fn这个函数执行。

// 自己模拟 call
Function.prototype.myCall = function(context){
  // 1. 让fn中的this变为context（obj）
  // eval(this.toString().replace("this", "obj"));
  // 2. 让fn执行
  this();
};
fn.myCall(obj);
```

## apply call 与 bind（lazy版本）

```javascript
fn.apply(obj, [1, 2]);
var tmp = fn.bind(obj, 1, 2);
tmp();
```











## Array.prototype.slice

```javascript
var ary = [1,2,3];
//ary.slice
// ary这个实例通过原型链的查找机制找到Array.prototype上的slice方法
```



# json 与数据绑定

最简单的前后台交互的模型

前后端通信约定的数据格式——目前主流是json

做web开发，你必须对一切细节了如指掌——我们在浏览器地址栏中键入地址，enter后发生的一切！

json只是一种特殊的数据格式，它是对象数据类型的。

```javascript
var jsonObj = {
  "name": "rose",
  "age": 19
};
```

## 重要方法

在window浏览器对象中，有个JSON属性，里面包含两个方法

1. JSON.parse 把json格式的字符串转为JSON对象
2. JSON.stringify 

在IE6,7中没有这两个方法



# 数据绑定

## 字符串拼接

字符串拼接要添加的html。会影响原来的元素。

但是实践中，多数使用这种方法。很多模板引擎也使用这种方法。

```javascript
oUl.innerHTML += str;
```



## 创建新节点

对原来的元素没有任何影响。

一次节点添加，就引起一次dom回流。

## 回流（reflow）与重绘

1. 回流

页面有元素添加或删除或移动，浏览器就重排和渲染页面。

2. 重绘

某元素的部分样式改变，不引起页面重排。

## 文档碎片

```javascript
var frg = document.createDocumentFragment();
// 创建一个文档碎片，相当于临时创建一个容器。
for(var i=0; i<ary.length; i++){
  var cur = ary[i];
  var oLi = document.createElement("li");
  oLi.innerHTML = "<span>" + (i + 4) + "</span>" + cur.title;
  frg.appendChild(oLi); // 放在文档碎片中
}
oUl.appendChild(frg); // 只引发一次回流
frg = null;



```



