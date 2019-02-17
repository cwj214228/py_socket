import socket

#实例的初始化
clinet=socket.socket()

#自定义服务器的ip和端口
ip_port=("127.0.0.1",8888)

#连接主机
clinet.connect(ip_port)

#接受主机信息
data=clinet.recv(1024)

#打印服务器返回的数据
print(data.decode())

#定义一个循环，不断地发送消息
while True:
    #输入发送的消息
    msg_input=input('请输入发送的消息：')

    #发送消息
    clinet.send(msg_input.encode())

    #接受服务器返回的数据
    data=clinet.recv(1024)

    #打印服务器返回的数据
    print(data.decode())

    if msg_input=='exit':
        break




