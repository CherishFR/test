import socket,os,hashlib
server = socket.socket()
server.bind(('localhost',9999))
server.listen()

while True:
    conn,addr = server.accept()
    print('new coon',addr)
    while True:
        data = conn.recv(1024) # 接收命令
        if data == 0 :
            print('连接已断开')
            break

        cmd,filename = data.decode().split() # 切割，分别赋值给cmd和filename
        if os.path.isfile(filename): # 如果存在同名的文件
            f = open(filename,'rb')
            file_size=os.stat(filename).st_size # 查看文件大小
            conn.send(str(file_size).encode()) # 发送文件大小
            conn.recv(1024) # 接受确认
            m = hashlib.md5() # 生成一个md5的hash对象
            for line in f:
                conn.send(line) # 发送文件数据
                m.update(line) # 向hash对象中添加内容
            f.close()
            conn.send(m.hexdigest().encode()) # 发送hash结果
        print('send done')
server.close()