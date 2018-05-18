# JPA 简介



# 类介绍

```java
JPA vs Hibernate
EntityManagerFactory---SessionFactory
EntityManager---Session
Transaction
```

## EntityManager

**（相当于hibernate的session）**

### 方法

1. find
2. getReference **相当于session的load方法---懒加载**

如果在加载对象之前，session已经关闭，会触发懒加载异常

3. persist **类似hibernate的save方法**

使对象由临时状态变为持久化状态。

与save方法的不同：save方法可以设置id，persist不可以。

4. remove **类似hibernate的delete**

**注意** remove只能删除持久化对象。 需要find获得持久化对象。

而delete方法还可以作用于游离对象。（new 出来的，尚未与数据库对象建立联系）

```java
Custumor customer = entityManager.find(Customer.class, 2);
entityManager.remove(customer);
```

