import threading
import time
import random
import socket
import sys

class rs:
    def rsListenPort(self,port):
        DNSfile = open('PROJI-DNSRS.txt', 'r')
        dnsTable = {}
        line = DNSfile.readline()
        while line:
            line = line.replace('\n','')
            entry = line.split(' ')
	    print(entry)
            dnsTable[entry[0]] = entry[1:]
            line = DNSfile.readline()
        print(dnsTable)
        try:
            ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[S]: Server socket created")
        except socket.error as err:
            print('{} \n'.format("socket open error ", err))
        server_binding = (socket.gethostname(), port)
        ss.bind(server_binding)
        ss.listen(1)
        host = socket.gethostname()
        print("[S]: Server host name is: ", host)
        localhost_ip = (socket.gethostbyname(host))
        print("[S]: Server IP address is  ", localhost_ip)
        csockid, addr = ss.accept()
        dnsTableb = {
            'qtsdatacenter.aws.com': ['128.64.3.2','A'],
            'mx.rutgers.edu': ['192.64.4.2', 'A'],
            'kill.cs.rutgers.edu': ['182.48.3.2', 'A'],
            'www.ibm.com': ['64.42.3.4','A'],
            'google.com': ['8.6.4.2', 'A'],
            'localhost': ['', 'NS']
            }
        word = csockid.recv(200).decode('utf-8')
        while word:
            bool = False
            if word == "exit":
                break
            for key in dnsTable.keys():
                if word.lower() == key.lower():
                    jenkins = dnsTable.get(key)
                    bool = True
                    break
                else:
                    jenkins = dnsTable.get(key)
                    if jenkins[0] == "-":
                        tsHostname = key;
            if bool:
                message = word + " " + jenkins[0] + " " + jenkins[1]
            else:
                message = tsHostname + " - NS";
            csockid.send(message.encode('utf-8'))
            word = csockid.recv(200).decode('utf-8')

        ss.close()
        exit()

if __name__ == '__main__':
        script = sys.argv[0]
        portnumber = int(sys.argv[1])
        foom = rs()
        foom.rsListenPort(portnumber);
