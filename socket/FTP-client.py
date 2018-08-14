import socket,hashlib
client = socket.socket()
client.connect(('localhost',9999))
while True:
    cmd = input('>>:').strip()
    if cmd == 0:
        continue
    if cmd.startswith('get'): # 判断是否以get开头
        client.send(cmd.encode()) # 发送命令
        file_size = int(client.recv(1024).decode()) # 接收数据大小信息
        print('文件大小为：',file_size)
        client.send('ack'.encode()) #确认开始接收数据
        new_size = 0
        filename = cmd.split()[1] # 提取文件名
        f=open(filename + '_new','wb')
        m=hashlib.md5() # 生成一个md5的hash对象
        while file_size >new_size:
            if file_size-new_size>1024: # 这个判断语句用来防止粘包
                size = 1024
            else:
                size = file_size - new_size
            data=client.recv(size) # 接收数据
            new_size+=len(data) # 记录接收数据的大小
            m.update(data) # 向hash对象中添加内容
            f.write(data) # 将数据写入文件
        else:
            print('文件接收完毕',file_size,new_size)
            f.close()
            recv_m = client.recv(1024)# 接收服务器计算的hash结果
            print('收到的MD5:',recv_m)
            print('计算的MD5:',m.hexdigest()) # 显示本地计算的hash结果，通过比对hash值是否一致，确保数据完整性
client.close()