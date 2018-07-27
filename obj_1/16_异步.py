import time
import _thread

def long_io(cb):
    def fun(callback):
        print('开始执行耗时操作')
        time.sleep(5)
        print('结束执行耗时操作')
        result = 'io result'
        callback(result)
    _thread.start_new_thread(fun,(cb,))

def on_finish(ret):
    # 回调函数
    print('开始执行回调函数')
    print(ret)
    print('结束执行回调函数')

def rep_a():
    print('开始处理请求A')
    long_io(on_finish)
    print('离开处理请求A')

def rep_b():
    print('开始处理请求B')
    print('完成处理请求B')

def main():
    rep_a()
    rep_b()
    while 1:
        pass

if __name__ == '__main__':
    main()