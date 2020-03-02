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
        line.lower()
        while line:
            line = line.replace('\n','')
            entry = line.split(' ');
            dnsTable[entry[0]] = entry[1:]
            line = DNSfile.readline()
            line.lower()
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
            if word == "exit":
                break
            print(word)
            for key in dnsTable.keys():
                if word.lower() == key.lower():
                    if word == "MX.RUTGERS.EDU":
                        print("yes")
                    jenkins = dnsTable.get(key)
                    print("this",jenkins)
                    break
                else:
                    jenkins = dnsTable.get('localhost')
            message = word + " " + jenkins[0] + " " + jenkins[1]
            print(message)
            csockid.send(message.encode('utf-8'))
            word = csockid.recv(200).decode('utf-8')

        ss.close()
        exit()

if __name__ == '__main__':
        script = sys.argv[0]
        portnumber = int(sys.argv[1])
        foom = rs()
        foom.rsListenPort(portnumber);
