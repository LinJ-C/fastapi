import socket

soct = socket.socket()
soct.bind(("127.0.0.1",8080))
soct.listen(3)
while 1:
    conn, addr = soct.accept()
    data = conn.recv(2048)
    print(addr)
    print("客户端接收到的数据：\n",data)
    conn.send(b'HTTP/1.1 200 Ok \r\n Server:linwar\r\n Refer=linwar \r\ncontent-type:text/plain \r\n\r\n{"userid":101}')
    conn.close()