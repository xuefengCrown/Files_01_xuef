官方文档

https://docs.spring.io/spring-data/data-jpa/docs/current/reference/html/



## Spring Data _ JPA

```xml
applicationContext.xml
<!-- 1. 配置数据源-->
<!-- 2. 配置JPA的EntityManagerFactory-->
<!-- 3. 配置事务管理器-->
<!-- 4. 配置支持注解事务-->
<!-- 5. 配置Spring Data-->
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xmlns:tx="http://www.springframework.org/schema/tx"
    xmlns:jpa="http://www.springframework.org/schema/data/jpa"
    xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
    http://www.springframework.org/schema/data/jpa http://www.springframework.org/schema/data/jpa/spring-jpa-1.3.xsd
    http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx-4.0.xsd
    http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.0.xsd">
    
    
    <!-- 配置自动扫描的包 -->
    <context:component-scan base-package="com">
    </context:component-scan>
    
    <!-- 配置数据源(数据库连接池) -->
    <context:property-placeholder location="classpath:db.properties"/>
    <bean id="dataSource"
        class="com.mchange.v2.c3p0.ComboPooledDataSource">
        <property name="user" value="${jdbc.user}"></property>    
        <property name="password" value="${jdbc.password}"></property>    
        <property name="driverClass" value="${jdbc.driverClass}"></property>    
        <property name="jdbcUrl" value="${jdbc.jdbcUrl}"></property>    
    </bean>
    
    <!-- 配置 JPA 的 EntityManagerFactory -->
  	<!--
		如何测试这个配置? 创建一个实体类，如果数据库能生成对应的table，说明配置成功。
	-->
    <bean id="entityManagerFactory"
        class="org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean">
        <property name="dataSource" ref="dataSource"></property><!-- 添加数据源 -->
      <!--JPA实现产品的适配器-->
        <property name="jpaVendorAdapter">
            <bean class="org.springframework.orm.jpa.vendor.HibernateJpaVendorAdapter"></bean>
        </property>    
      <!--要扫描的配置了@Entity注解的包-->
        <property name="packagesToScan" value="com.entity"></property>
        <!-- 配置JPA属性；实际上是JPA实现产品（此处即hibernate）的属性 -->
        <property name="jpaProperties">
            <props>
              	<!--实体类的属性名与数据表的列名之间的映射策略-->
                <prop key="hibernate.ejb.naming_strategy">
                  org.hibernate.cfg.ImprovedNamingStrategy</prop>
                <prop key="hibernate.hbm2ddl.auto">none</prop>
                <prop key="hibernate.show_sql">true</prop>
                <prop key="hibernate.format_sql">true</prop>
                <!-- 数据库方言； hibernate 并不知道自己要使用哪种数据库 -->
                <prop key="hibernate.dialect">org.hibernate.dialect.MySQL5InnoDBDialect</prop>
                <!--  
                <prop key="hibernate.cache.use_second_level_cache">true</prop>
                <prop key="hibernate.cache.region.factory_class">
					org.hibernate.cache.ehcache.EhCacheRegionFactory</prop>
                <prop key="hibernate.cache.use_query_cache">true</prop>
                -->
            </props>
        </property>
        <!--  <property name="sharedCacheMode" value="ENABLE_SELECTIVE"></property>-->
    </bean>
    
    <!-- 配置事务 纯事务 jpa事务 -->
    <bean id="transactionManager"
        class="org.springframework.orm.jpa.JpaTransactionManager">
        <property name="entityManagerFactory" ref="entityManagerFactory"></property>    
    </bean>
    
    <!-- 配置支持基于注解的事务 -->
    <tx:annotation-driven transaction-manager="transactionManager"/>
    
    <!-- 配置 SpringData -->
    <jpa:repositories base-package="com.dao"
        entity-manager-factory-ref="entityManagerFactory"></jpa:repositories>
    
</beans>
```

### Repository 接口

1. 一个空接口，即一个标记接口
2. 若我们定义的接口继承了它，则该接口会被IOC容器识别为一个Repository Bean。（代理类）纳入到IOC容器中，进而可以在该接口中定义满足一定规范的方法。（注意在配置spring data时，将该接口所在的包添加进扫描路径）
3. 实际上，可以用注解来代替继承Repository接口@RepositoryDefinition(domainClass=Person.class,idClass=Integer.class)
4. Repository有一些子接口，为我们提供了一些方法。选中， C^T查看类继承结构

### Repository查询方法定义规范

```java
1. getByLastNameStartingWithAndIdLessThan(String lastName, Integerid)
2. 支持级联查询
getByAddress_IdGreaterThan(Integer id)
3. 有很多关键词，自己去查
4. 不够灵活。自己可以使用@Query去自己定制（下一节）

```

#### @Query 自定义JPQL语句以实现灵活的查询

```java
@Query("select p from Person p where p.id = (select max(p2.id) from Person p2)")
Person getMaxIdPerson();

2. 传递参数 ?1 ?2
  or :lastName :email
  (@Param("lastName") String lastName, ..)
3. 原生sql
nativeQuery=true
```





### 实现带通用条件的分页查询



## Spring Boot 下的Spring Data JPA

### Quick Start

- <https://projects.spring.io/spring-data/#quick-start>

#### Steps

1. 引入依赖

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
```

2. 编写实体类**Entity**

```java
@Entity
public class Employee {

  private @Id @GeneratedValue Long id;
  private String firstName, lastName, description;

  private Employee() {}

  public Employee(String firstName, String lastName, String description) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.description = description;
  }
}
```

3. 持久化操作的接口

```java
public interface EmployeeRepository extends CrudRepository<Employee, Long> {

  Employee findByFirstName(String firstName);

  List<Employee> findByLastName(String lastName);
}
```

