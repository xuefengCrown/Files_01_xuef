# Redis 讲解

《Redis 设计与实现》

## install

```bash
linux 下

https://redis.io/download

```

## 基本操作

```bash
> redis-cli
>> set a b
>> get a
"b"

# 查看所有 key
>> keys *

# 带过期时间的 set
setex(key, 10, val)

# 如何更新文章，网页浏览人数
# 不可能直接对数据库进行 update
# update 是需要对表中记录加锁的，所以效率会很低
# 应该先在内存中操作，找个时间再保存到数据库
set("pv", 100)
incr("pv")
incrBy("pv", 10)

# 秒杀系统。高并发操作如何应对
《淘宝技术10年》

# 最近来访。用户最近浏览

# 临时加字段
jedis.hset("user1", "name", "rose");

# 不存在时插入
jedis.hsetnx("user1", "groupId", "java")

# 集合操作
jedis.sadd
#（交集：共同好友）
jedis.sinter
# 是否已经点赞
jedis.sismember
# 移动
smove
# 元素个数
scard

# 排行榜
优先队列
jedis.zadd("rankKey", 15, "jack");
jedis.zadd("rankKey", 40, "rose");
jedis.zincrBy("rankKey", 2, "rose"); // 提高 2 分

// 前三名
jedis.zrange("rankKey", 1, 3);

// 查询名次
zrank


微博大量使用了 redis

用户登录的 token
天然的可以放在 redis，添加一个 有效期

```



## 配置文件

/etc/redis/redis.conf



# redis 实际应用

## redis在牛客

PV
点赞
关注（我关注谁，谁关注我都是一个个集合）
排行榜
验证码
缓存

​	mysql外包着一层缓存。对于用户头像，用户名等数据，一般不变，除非修改。

​	我们可以把它们放在redis中，访问时，优先去缓存里（redis）取，如果修改了，就让缓存失效

​	（删除redis中对应数据）

异步队列

​	发生了什么事情后（点赞，评论），就抛一个事件进redis的一个list中，然后专门有一个线程

​	来处理这些事件。（取出事件，比如点赞，然后给用户发邮件或站内信）

判题队列

​	区分编题空闲期和高峰期。高峰期就得加机器来编译和判题。

