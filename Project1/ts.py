import threading
import time
import random
import sys
import socket

class ts:
    @staticmethod
    def tsListenPort(port):
        DNSfile = open('PROJI-DNSTS.txt', 'r')
        try:
            ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[S]: Server socket created")
        except socket.error as err:
            print('{} \n'.format("socket open error ", err))
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
            if(word is "exit"):
                break
            print("hello")
            print(word)
            if word.lower() in dnsTable.keys():
                jenkins = dnsTable.get(word)
                message = word + " " + jenkins[0] + " " + jenkins[1]
                print(message)
                csockid.send(message.encode('utf-8'))
            else:
                jenkins = dnsTable.get('localhost')
                message = word + jenkins[0]
                print(message)
                csockid.send(message.encode('utf-8'))
            print("about to take next word")
            word = csockid.recv(200).decode('utf-8')
            print("got next word")
            word.lower()

        print("made it out of loop")
        ss.close()
        exit()
if __name__ == '__main__':
        script = sys.argv[0]
        portnumber = int(sys.argv[1])
        ts.tsListenPort(portnumber)
