# coding:utf-8

import threading
from Queue import Queue
from lxml import etree
import requests
import json

class ThreadCrawl(threading.Thread):
    def __init__(self,threadName,pageQueue,dataQueue):
        super(ThreadCrawl,self).__init__()
        # 线程名
        self.threadName = threadName
        # 页码队列
        self.pageQueue = pageQueue
        # 数据队列
        self.dataQueue = dataQueue
        # 请求报头
        self.headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    def run(self):
        while not CRAWL_EXIT:
            try:
                # 取出一个数字，先进先出
                # 可选参数block，默认为True（如果队列为空，block = True就会进入阻塞状态，直到队列有新的数据；如果block = False就会弹出异常）
                page = self.pageQueue.get(False)
                url = "http://www.qiushibaike.com/8hr/page/"+str(page)+"/"
                content = requests.get(url,headers=self.headers)
                self.dataQueue.put(content)
            except:
                pass


class ThreadParse(threading.Thread):
    def __init__(self,threadName,dataQueue,filename):
        super(ThreadParse,self).__init__()
        # 线程名
        self.threadName = threadName
        # 数据队列
        self.dataQueue = dataQueue
        # 保存后的文件名
        self.filename = filename
    def run(self):
        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)
                self.parse(html)
            except:
                pass
    def parse(self,html):
        html = etree.HTML(html)
        node_list = html.xpath('//div[contains(@id, "qiushi_tag")]')

        for node in node_list:
            # xpath返回的列表，这个列表就这一个参数，用索引方式取出来，用户名
            username = node.xpath('./div/a/@title')[0]
            # 图片连接
            image = node.xpath('.//div[@class="thumb"]//@src')
            # 取出标签下的内容,段子内容
            content = node.xpath('.//div[@class="content"]/span')[0].text
            # 取出标签里包含的内容，点赞
            zan = node.xpath('.//i')[0].text
            # 评论
            comments = node.xpath('.//i')[1].text

            items = {
                "username": username,
                "image": image,
                "content": content,
                "zan": zan,
                "comments": comments
            }

            # with 后面有两个必须执行的操作：__enter__ 和 _exit__
            # 不管里面的操作结果如何，都会执行打开、关闭
            # 打开锁、处理内容、释放锁
            with open("qiushi.json", "a") as f:
                f.write(json.dumps(items, ensure_ascii=False).encode("utf-8") + "\n")


CRAWL_EXIT = False
PARSE_EXIT = False

def main():
    # 定义页码的队列，可以存储10页
    pageQueue = Queue(10)
    # 放入1-10的数字，先进先出
    for i in range(1,11):
        pageQueue.put(i)

    # 采集结果（每一页的HTML源码）的数据队列，参数为空表示不限制
    dataQueue = Queue()

    filename = open("duanzi.json","a")

    # 创建线程锁
    lock = threading.Lock()

    # 采集线程的名字
    crawlList = ["采集线程1","采集线程2","采集线程3"]

    # 存储三个采集线程
    threadcrawl = []

    # 创建三个线程来完成收集10页HTML文件的任务
    for threadName in crawlList:
        thread = ThreadCrawl(threadName,pageQueue,dataQueue)
        thread.start()
        threadcrawl.append(thread)

    # 解析线程的名字
    parseList = ["解析线程1", "解析线程2", "解析线程3"]

    # 存储三个解析线程
    threadparse = []

    # 创建三个线程来完成解析10页HTML文件的任务
    for threadName in parseList:
        thread = ThreadParse(threadName,dataQueue,filename)
        thread.start()
        threadparse.append(thread)

    # 等待pageQueue队列为空，也就是等待之前的操作执行完毕
    while not pageQueue.empty():
        pass
    # 如果pageQueue为空，采集线程退出循环
    global CRAWL_EXIT
    CRAWL_EXIT = True
    # 阻塞主线程，否则主线程执行完毕不管子线程是否结束都会退出
    for thread in threadcrawl:
        thread.join()  # 验证线程是否结束，没有结束则阻塞，至到线程结束

    while not dataQueue.empty():
        pass
    global PARSE_EXIT
    PARSE_EXIT = True
    for thread in threadparse:
        thread.join()
        print
    with lock:
        # 关闭文件
        filename.close()
    print "谢谢使用！"


if __name__ == '__main__':
    main()