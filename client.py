import socket

ip= socket.gethostname()
port =1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))
con =True
while con:
    msg = input("enter Messgae:")
    s.send(msg.encode("utf-8"))
    if msg == "quit":
        con = False    
s.close()