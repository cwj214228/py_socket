import socket

#实例化模块
sk=socket.socket()

#定义连接ip和端口
ip_port=('127.0.0.1',9999)

#绑定ip和端口
sk.bind(ip_port)

#定义最大连接数
sk.listen(5)

#进入循环
while True:
    #等待客户端连接
    conn,adress=sk.accept()

    #一直使用当前连接，直到结束
    while True:
        #打开文件等待数据写入
        with open('file','ab')as f:
            #接收数据
            data=conn.recv(1024)

            if data==b'quit':
                break

            #写入文件
            f.write(data)
        #发送完成标志
        conn.send('success'.encode())
#关闭连接
sk.close()
