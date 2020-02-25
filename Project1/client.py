import threading
import time
import random
import sys
import socket as mysoc

class client:

    def rsHostname():
        print("place holder")

    def rsListenPort(line):
        cs.send(line.encode('utf-8'))
        data=cs.recv(100).decode('utf-8')
        print(data,"\n")
        if not data[len(data)-1] == 'A':
            return False
        return True

    def tsListenPort(line):
        print(line," not found")

if __name__ == '__main__':
    args = sys.argv
    rsHostName = args[1]
    rsPort = int(args[2])
    tsPort = int(args[3])
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
    sa_sameas_myaddr =mysoc.gethostbyname(mysoc.gethostname())

    rs_binding=(sa_sameas_myaddr,rsPort)
    cs.connect(rs_binding)

    #ts_binding=(sa_sameas_myaddr,tsPort)
    #cs.connect(ts_binding)


    input = open("PROJI-HNS.txt","r")
    while True:
        lines = input.readlines()
        for line in lines:
            line = line.rstrip("\n")
            if not client.rsListenPort(line):
                client.tsListenPort(line)
