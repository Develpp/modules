import os
from time import sleep as delay
def send(file,s):
	s.send("OK")
	drain=s.recv(1024)
	if drain == "OK":pass
	else:return -1
	repeat=os.path.getsize(file)/65535+1
	s.send(str(repeat))
	delay(0.5)
	data=open(file,"rb")
	i=0
	s.send("OK")
	if s.recv(1024) == "OK":pass
	else:return -1
	while i < repeat:
		if s.recv(1024) == "OK":pass
		else:return -1
		s.send(data.read(65535))
		i+=1
def recv(save,s):
	open(save,"w").close()
	if s.recv(1024) == "OK":s.send("OK")
	else:return -1
	repeat=int(s.recv(999999))
	i=0
	if s.recv(1024) == "OK":s.send("OK")
	else:return -1
	while i < repeat:
		s.send("OK")
		open(save,"a").write(s.recv(65535))
		i+=1
