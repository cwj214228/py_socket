import socketserver

#定义一个类
class MyServer(socketserver.BaseRequestHandler):
    #如果handle()方法报错，则会进行跳过
    #setup()和finish()无论如何都会执行
    #首先执行setup()
    def setup(self):
        pass

    #然后执行handle()
    def handle(self):
        #定义连接变量
        conn=self.request

        #发送消息
        msg='Hello World!'

        #发送消息
        conn.send(msg.encode())

        while True:
            #接受客户端消息
            data=conn.recv(1024)

            #打印消息
            print(data)

            #如果接收到exit，则退出循环
            if data==b'exit':
                break

            #向客户端发送消息
            conn.send(data)

        conn.close()

    #最后执行finish()
    def finish(self):
        pass

if __name__ == '__main__':
    #创建多线程实例
    server=socketserver.ThreadingTCPServer(('127.0.0.1',8888),MyServer)

    #开启多线程
    server.serve_forever()