import threading
import time
import random
import sys
import socket

class ts:
    @staticmethod
    def tsListenPort(port):
        DNSfile = open('PROJI-DNSTS.txt', 'r')
        dnsTable = {}
        line = DNSfile.readline()
        while line:
            line = line.replace('\n','')
            entry = line.split(' ');
            dnsTable[entry[0]] = entry[1:]
            line = DNSfile.readline()
        print(dnsTable)
        while True:
            try:
                ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print("[S]: Server socket created")
            except socket.error as err:
                print('{} \n'.format("socket open error ", err))
            server_binding = ('', port)
            ss.bind(server_binding)
            ss.listen(1)
            host = socket.gethostname()
            print("[S]: Server host name is: ", host)
            localhost_ip = (socket.gethostbyname(host))
            print("[S]: Server IP address is  ", localhost_ip)
            csockid, addr = ss.accept()

            word = csockid.recv(200).decode('utf-8')
            word.lower()
            dnsTableb = {
                'qtsdatacenter.aws.com': ['128.64.3.2', 'A'],
                'www.rutgers.edu': ['192.64.4.4', 'A'],
                'mx.rutgers.edu': ['192.64.4.5', 'A'],
                'grep.cs.princeton.edu': ['182.48.3.2', 'A'],
                'www.ibm.com': ['64.42.3.4', 'A'],
                'google.com': ['8.7.45.2', 'A'],
                'localhost' : ['-Error: HOST NOT FOUND', '']
            }

            while word:
                if word == "exit":
                    break
                bool = False
                for key in dnsTable.keys():
                    if word.lower() == key.lower():
                        jenkins = dnsTable.get(word.lower())
                        message = word + " " + jenkins[0] + " " + jenkins[1]
                        csockid.send(message.encode('utf-8'))
                        bool = True
                        break
                if not bool:
                    message = word + " - Error:HOST NOT FOUND"
                    csockid.send(message.encode('utf-8'))
                break

        ss.close()
        exit()

if __name__ == '__main__':
        script = sys.argv[0]
        portnumber = int(sys.argv[1])
        ts.tsListenPort(portnumber)
