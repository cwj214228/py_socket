import socket

#实例化模块
sk=socket.socket()

#定义连接ip和端口
ip_port=('127.0.0.1',9999)

#进行服务器的连接
sk.connect(ip_port)

#打开文件
with open('py_client.py','rb')as f:
    #按每一段分割文件
    for i in f:
        #文件上传
        sk.send(i)

        #判断服务器是否真的完成写入数据
        data=sk.recv(1024)
        if data!=b'success':
            break


#给服务器端发送结束信号
sk.send('quit'.encode())

