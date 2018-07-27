import time
import _thread



def long_io():
    print('开始执行耗时操作')
    time.sleep(5)
    print('结束执行耗时操作')
    result = 'io result'
    yield result

def gen_coroutine(f):
    def inner():
        gen = f()
        gen_long_io = gen.__next__()
        def fun():
            ret = gen_long_io.__next__()
            try:
                gen.send(ret)
            except StopIteration:
                pass
        _thread.start_new_thread(fun, ())
    return inner

@gen_coroutine
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
    rep_a()
    rep_b()
    while 1:
        pass

if __name__ == '__main__':
    main()