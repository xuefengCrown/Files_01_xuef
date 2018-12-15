#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#用asyncio的异步网络连接来获取sina、sohu和163的网站首页

import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

"""
计算机运行的时候，计算是在CPU上进行的，但是IO操作是在计算机其他硬件进行的。
但是例如你进行一个网络请求的传统过程是这样的：
.....cpu.....
-发起网络请求
-交给网卡
.....cpu进入等待，等待网卡反馈.....

.....网卡.....
-发送http
-接收http
-反馈给cpu
.....网卡工作结束.....

.....CPU.....
-接收到网卡反馈
-处理信息
-完成，开始下一条，
-发起网络请求
-交给网卡
-...

如果是多条网络请求，每次发送给网卡都需要等待网卡把请求信息反馈给CPU，然后CPU一条一条的处理。
但是协程是最大化利用IO和CPU
"""
