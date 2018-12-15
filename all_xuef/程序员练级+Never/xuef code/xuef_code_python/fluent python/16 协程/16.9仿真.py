
#揭示了如何使用协程在单个线程中管理并发活动。
"""
使用案例：使用协程做离散事件仿真
协程能自然地表述很多算法，例如仿真、游戏、异步 I/O，以及其
他事件驱动型编程形式或协作式多任务。
"""
#通过仿真系统能说明如何使用协程代替线程实现并发的活动，
#而且对理解第 18 章讨论的 asyncio 包有极大的帮助。

##SimPy 是一个实现离散事件仿真的Python 包，
##通过一个协程表示离散事件仿真系统中的各个进程。

##在仿真领域，进程这个术语指代模型中某个实体的活动，与
##操作系统中的进程无关。仿真系统中的一个进程可以使用操作系统
##中的一个进程实现，但是通常会使用一个线程或一个协程实现。

##这一付出能得到很大回报，让我们洞悉asyncio、Twisted 和 Tornado 等库
##是如何在单个线程中管理多个并发活动的。

####################################
#四处徘徊和行程所用的时间使用指数分布生成。
#离散事件仿真经常使用指数分布。
#你会看到一些非常短的行程，你就假设那是一个雨天，一些乘客坐出租车只走了一个街区。
#在理想的城市中，即使下雨也有出租车。


#compute_delay 函数，返回单位为分钟的时间间隔;
#Event类，一个 namedtuple，定义方式如下：
##Event = collections.namedtuple('Event', 'time proc action')
##在 Event 实例中，time 字段是事件发生时的仿真时间，proc 字段是出
##租车进程实例的编号，action 字段是描述活动的字符串。
import random
import collections
import queue


Event = collections.namedtuple('Event', 'time proc action')

#taxi_sim.py：taxi_process 协程，实现各辆出租车的活动
##每辆出租车调用一次 taxi_process 函数，创建一个生成器对象，表示各辆出租车的运营过程。
##ident 是出租车的编号（如上述运行示例中的 0、1、2）;
##trips 是出租车回家之前的行程数量;
##start_time是出租车离开车库的时间。
def taxi_process(ident, trips, start_time=0): #➊
    """每次改变状态时创建事件，把控制权让给仿真器"""
    time = yield Event(start_time, ident, 'leave garage') #➋
    #产出的第一个 Event 是 'leave garage'。执行到这一行时，协程
    #会暂停，让仿真主循环着手处理排定的下一个事件。需要重新激活这个
    #进程时，主循环会发送（使用 send 方法）当前的仿真时间，赋值给time。
    
    for i in range(trips): #➌每次行程都会执行一遍这个代码块。
        #产出一个 Event 实例，表示拉到乘客了。协程在这里暂停。
        #需要重新激活这个协程时，主循环会发送（使用 send 方法）当前的时间。
        time = yield Event(time, ident, 'pick up passenger') #➍
        
        #产出一个 Event 实例，表示乘客下车了。协程在这里暂停，
        #等待主循环发送时间，然后重新激活。
        time = yield Event(time, ident, 'drop off passenger') #➎

    #指定的行程数量完成后，for 循环结束，最后产出 'going home'事件。此时，协程最后一次暂停。
    yield Event(time, ident, 'going home') #➏
    # 出租车进程结束➐协程执行到最后时，生成器对象抛出 StopIteration 异常。

"""
#创建一个生成器对象，表示一辆出租车。
#这辆出租车的编号是13（ident=13），从 t=0 时开始工作，有两次行程。
taxi = taxi_process(ident=13, trips=2, start_time=0) #➊

next(taxi) #➋
#Event(time=0, proc=13, action='leave garage')

taxi.send(_.time + 7) #➌
#Event(time=7, proc=13, action='pick up passenger') ➍
taxi.send(_.time + 23) #➎
#Event(time=30, proc=13, action='drop off passenger')
taxi.send(_.time + 5) #➏
#Event(time=35, proc=13, action='pick up passenger')
taxi.send(_.time + 48) #➐
#Event(time=83, proc=13, action='drop off passenger')
taxi.send(_.time + 1)
#Event(time=84, proc=13, action='going home') ➑
taxi.send(_.time + 10)
"""

DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5


def compute_duration(previous_action):
    """Compute action duration using exponential distribution"""
    if previous_action in ['leave garage', 'drop off passenger']:
        # new state is prowling
        interval = SEARCH_DURATION
    elif previous_action == 'pick up passenger':
        # new state is trip
        interval = TRIP_DURATION
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('Unknown previous_action: %s' % previous_action)
    return int(random.expovariate(1/interval)) + 1

class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue() #
        #一个字典，把出租车的编号映射到仿真过程中激活的进程（表示出租车的生成器对象）。
        self.procs = dict(procs_map)

    def run(self, end_time): #➊
        """排定并显示事件，直到时间结束"""
        # 排定各辆出租车的第一个事件
        for _, proc in sorted(self.procs.items()): #➋
            first_event = next(proc) #➌
            self.events.put(first_event) #➍

        # 这个仿真系统的主循环
        sim_time = 0 #➎
        while sim_time < end_time: #➏
            if self.events.empty(): #➐
                print('*** end of events ***')
                break
            current_event = self.events.get() #➑
            sim_time, proc_id, previous_action = current_event #➒
            print('taxi:', proc_id, proc_id * ' ', current_event) #➓
            active_proc = self.procs[proc_id] #⓫
            
            next_time = sim_time + compute_duration(previous_action) #⓬
            try:
                next_event = active_proc.send(next_time) #⓭
            except StopIteration:
                del self.procs[proc_id] #⓮
            else:
                self.events.put(next_event) #⓯
        else: #⓰
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))


def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS,
         seed=None):
    """Initialize random generator, build procs and run simulation"""
    if seed is not None:
        random.seed(seed)  # get reproducible results

    taxis = {i: taxi_process(i, (i+1)*2, i*DEPARTURE_INTERVAL)
             for i in range(num_taxis)}
    sim = Simulator(taxis)
    sim.run(end_time)

if __name__ == '__main__':
    main()



"""
这个示例的要旨是说明如何在一个主循环中处理事件，以及如何通过发
送数据驱动协程。这是 asyncio 包底层的基本思想，我们在第 18 章会
学习这个包。
"""











