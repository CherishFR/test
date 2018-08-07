import socket
server = socket.socket()  # 默认(AF.INET,sock.SOCK_STREAM)，AF.INET为IPv4协议，SOCK_STREAM为TCP协议
server.bind(('localhost',9999))  # 绑定要监听的端口
server.listen(5)  # 监听，最大允许多少链接
while True: #
    print('准备开始连接')
    conn,add=server.accept()  # 等客户端的链接,连接成功后会返还一个连接的实例以及地址信息
    print('conn:',conn,'add:',add)
    print('连接成功')
    while True:  # 持续接收，处理，发送数据
        data1=conn.recv(1024)  # 接受数据，赋给data1，一次最大接受1204比特
        print('recv:',data1)  # 对解码输出，byte类型的数据不会变
        if not data1:  # 防止客户端断开后由于服务器端无法收到数据进入死循环
            break
        conn.send(data1.upper())  # 将data1中的数据转为大写，再发送数据