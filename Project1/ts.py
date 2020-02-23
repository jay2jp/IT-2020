import threading
import time
import random
import socket

class ts:
    def tsListenPort(self):
        try:
            ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[S]: Server socket created")
        except socket.error as err:
            print('{} \n'.format("socket open error ", err))
        server_binding = ('', 50009)
        ss.bind(server_binding)
        ss.listen(1)
        host = socket.gethostname()
        print("[S]: Server host name is: ", host)
        localhost_ip = (socket.gethostbyname(host))
        csockid, addr = ss.accept()
        print("[S]: Server IP address is  ", localhost_ip)
        dnsTable = {
            'qtsdatacenter.aws.com': ['128.64.3.2', 'A'],
            'www.rutgers.edu': ['192.64.4.4', 'A'],
            'mx.rutgers.edu': ['192.64.4.5', 'A'],
            'grep.cs.princeton.edu': ['182.48.3.2', 'A'],
            'www.ibm.com': ['64.42.3.4', 'A'],
            'google.com': ['8.7.45.2', 'A'],
        }