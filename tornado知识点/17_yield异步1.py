import time
import _thread

gen = None

def long_io():
    def fun():
        global gen
        print('开始执行耗时操作')
        time.sleep(5)
        print('结束执行耗时操作')
        result = 'io result'
        try:
            gen.send(result)
        except StopIteration:
            pass
    _thread.start_new_thread(fun, ())

def rep_a():
    print('开始处理请求A')
    ret = yield long_io()
    print(ret)
    print('离开处理请求A')

def rep_b():
    print('开始处理请求B')
    time.sleep(2)
    print('完成处理请求B')

def main():
    global gen
    gen = rep_a()
    gen.__next__()
    rep_b()
    while 1:
        pass

if __name__ == '__main__':
    main()