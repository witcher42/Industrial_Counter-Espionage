# KAIS 2020 Competition
# Usage:
#       (DFE) sudo python Torpedo_Decoy.py 502
#       (ATT) nc [ip addr] 502
#

import asyncore
import socket
import os
import sys

class Decoy(asyncore.dispatcher_with_send):
    print 'Listening...\n'
    def handle_read(self):
        data=self.recv(1024)
        #self.send(data*411000110007) # Launch a Torpedo...!
        print data

class Deploy(asyncore.dispatcher):
    def handle_accept(self):
        conn = self.accept()
        if conn is not None:
            sock,addr = conn
            print addr[0]+' connected...'
            os.system("iptables -I INPUT -s "+addr[0]+" -j DROP")
            os.system("iptables -L | grep "+addr[0])
            print '\nDecoys Deployed...!\n'
            Decoy(sock)
        
    def __init__(self,port):
        self.port = port
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(("",port))
        self.listen(1)

if len(sys.argv)!=2:
    print 'Argc Error\n'
    print 'Example: python Torpedo_Decoy.py 502\n'
    sys.exit(2)

Deploy(int(sys.argv[1]))
asyncore.loop()
