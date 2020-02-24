import threading
import time
import random
import sys
import socket

class ts:
    def tsListenPort(self):
        try:
            ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[S]: Server socket created")
        except socket.error as err:
            print('{} \n'.format("socket open error ", err))
        server_binding = ('', 50007)
        ss.bind(server_binding)
        ss.listen(1)
        host = socket.gethostname()
        print("[S]: Server host name is: ", host)
        localhost_ip = (socket.gethostbyname(host))
        print("[S]: Server IP address is  ", localhost_ip)
        csockid, addr = ss.accept()

        word = csockid.recv(200).decode('utf-8')
        dnsTable = {
            'qtsdatacenter.aws.com': ['128.64.3.2', 'A'],
            'www.rutgers.edu': ['192.64.4.4', 'A'],
            'mx.rutgers.edu': ['192.64.4.5', 'A'],
            'grep.cs.princeton.edu': ['182.48.3.2', 'A'],
            'www.ibm.com': ['64.42.3.4', 'A'],
            'google.com': ['8.7.45.2', 'A'],
            'localhost' : ['-Error: HOST NOT FOUND', '']
        }
        while word:
            if word in dnsTable.keys:
                jenkins = dnsTable[word]
                message = word + " " + jenkins[0] + " " + jenkins[1]
                csockid.send(message.encode('utf-8'));
            else:
                jenkins = dnsTable['localhost']
                message = word + jenkins[0]
                csockid.send(message.encode('utf-8'));


        ss.close()
        exit()
    def main(self):
        script = sys.argv[0]
        portnumber = sys.argv[1]
        self.rsListenPort(portnumber);

    main(0)


