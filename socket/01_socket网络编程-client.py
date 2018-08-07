import socket
client=socket.socket()  # 声明socket类型，同时生成socket连接对象
client.connect(('localhost',9999))  # 向指定接口发起连接
# client.send(b'hello world')  建立连接后发送数据,在python3中只能发byte类型的数据
# client.send('这是网络编程'.encode('utf-8')) 中文需要编码成utf-8
while True:  # 实现持续发送，接收数据
    msg=input('>>').strip()
    if len(msg) == 0:  # 由于encode无法处理空数据，因此为了防止出错卡死需要在用户发送空数据时跳出本次循环
        continue
    client.send(msg.encode('utf-8'))  # 必须以byte类型输出
    data = client.recv(1024)  # 接受数据，赋给data，最大接受1024比特
    print('recv:',data.decode())  # 解码后输出
