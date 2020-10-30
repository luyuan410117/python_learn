#!/usr/bin/python3

def consumer():
    r = "init"                                                      # RUN	1.1
    while True:
        ### n 的值 = produce中c.send(n)传送过来的n的值，并将r的值通过yield传给produce，由c.send(n)接收
        print("coroutine before yield ...")                         # RUN	2	15	25	35	45	55
        # n = yield | n = (yield) 就变成了协程， 而yield r 则是一个生成器，把r的值给保留下来
        n = yield r                                                 # RUN	3	10	20	30	40	50
        print("coroutine after yield ...")                          # RUN		11	21	31	41	51
        if not n:                                                   # RUN		12(n=1)	22(n=2)	32(n=3)	42(n=4)	52(n=5)
            return 
        print("[CONSUMER] Consuming %s... r = %s" % (n, r))         # RUN		13	23	33	43	53
        r = "200 OK"                                                # RUN		14	24 	34	44	54

def produce(c):
    # 1. 首先调用c.send(None)启动生成器,返回值为""
    r = c.send(None)                                                # RUN	1
    print(r)                                                        # RUN	4 
    next(c)     # 也可以启动生成器
    n = 0                                                           # RUN	5
    while n < 5:                                                    # RUN	6
        ### produce or do something...
        n += 1   # 2.do something 1                                 # RUN	7		17	27	37	47
        print("[PRODUCE] Producing %d..." % n) # 2.do something n   # RUN	8(n=1)		18(n=2)	28(n=3)	38(n=4)	48(n=5)
        ### something done
        # 3. 通过c.send(n)切换到consumer去执行 r的值 = consumer中yield r中的r的值
        r = c.send(n)                                               # RUN	9		19	29	39	49
        print("[PRODUCE] Consumer return: %s" % r)                  # RUN		16	26	36	46	56
    c.close()

c = consumer()
produce(c)
"""
注意到consumer函数是一个generator，把一个consumer传入produce后：
首先调用c.send(None)启动生成器；
然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
consumer通过yield拿到消息，处理，又通过yield把结果传回；
produce拿到consumer处理的结果，继续生产下一条消息；
produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
"""
