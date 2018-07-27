import time

def long_io():
    print('开始执行耗时操作')
    time.sleep(5)
    print('结束执行耗时操作')
    result = 'io result'
    return result

def rep_a():
    print('开始处理请求A')
    long_io()
    print('完成处理请求A')

def rep_b():
    print('开始处理请求B')
    print('完成处理请求B')

def main():
    rep_a()
    rep_b()

if __name__ == '__main__':
    main()