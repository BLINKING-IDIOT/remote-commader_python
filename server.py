import socket	
from os import popen
s = socket.socket()		
print ("Socket successfully created")
ip=(popen("hostname -I | awk '{print $1}'").read()).strip()
port = 15450			

s.bind((ip, port))		

s.listen(5)	
print ("Started listening")		

while True:
    c, addr = s.accept()	
    print ('Got connection from', addr )
    x=""
    while x!="exit server":
        x=input("Enter the command to send:")
        c.send(x.encode())
        print(c.recv(1024).decode())
    c.close()
    break
