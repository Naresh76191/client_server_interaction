import socket

ip = socket.gethostname()
port= 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip,port))
s.listen(5)
print("Server Listening on")
socketclient, address = s.accept()
print("Connected From ", address)
msg = socketclient.recv(1024)
msg = msg.decode("utf-8")
print(msg)
while True:
    msg =socketclient.recv(1024).decode("utf-8")
    print("Received:",msg)
    if msg == "quit":
        print("client requested to quite. closing connection")
        socketclient.close()
        break
    response = "message received:" + msg
s.close()
