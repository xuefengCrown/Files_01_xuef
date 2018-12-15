
#协同程序
## ???同步的方式编写异步代码???我不是很理解
def get_content(url):
    html_c = download_html(url)# IO, 比较耗时; 我们希望能在此处悬停,切换到另一个函数去执行

    parse(html_c) # cpu计算 
    

# 我们希望能够有可以暂停的函数,并且可以在适当的时候恢复该函数的继续执行!!!
# 协程===可以暂停的函数(而且可以向暂停的地方传入值)


##yield from
## RESULT = yield from EXPR
## yield from 会在子生成器迭代完成之后(也就是抛了StopIteration as e后),取出e中的return val
## 交给 RESULT
