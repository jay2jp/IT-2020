import threading
import time
import random
import sys
import socket as mysoc

class client:

    def rsHostname():
        print("place holder")

    @staticmethod
    def rsListenPort(line):
        cs.send(line.encode('utf-8'))
        data=cs.recv(100).decode('utf-8')
        if not data[len(data)-1] == 'A':
            return False
        client.writeToFile(data)
        return True

    @staticmethod
    def tsListenPort(line):
        #print("trying ts",line)
        cs2.send(line.encode('utf-8'))
        print("yes")
        data=cs.recv(100).deocde('utf-8')
        print("i hope")
        client.writeToFile(data)
        print("I made it here")
        #if not data[len(data)-1] == 'A':
        #    return False
        #return True

    @staticmethod
    def writeToFile(line):
        output = open("RESOLVED.txt","a")
        output.write(line+"\n")
        output.close()

if __name__ == '__main__':
    args = sys.argv
    rsHostName = args[1]
    rsPort = int(args[2])
    tsPort = int(args[3])
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        cs2=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
    sa_sameas_myaddr = mysoc.gethostbyname(mysoc.gethostname())

    rs_binding=(sa_sameas_myaddr,rsPort)
    cs.connect(rs_binding)

    ts_binding=(sa_sameas_myaddr,tsPort)
    cs2.connect(ts_binding)

    input = open("PROJI-HNS.txt","r")
    lines = input.readlines()
    while True:
        for line in lines:
            print("hi")
            line = line.rstrip("\n")
            if not client.rsListenPort(line):
                client.tsListenPort(line)
    input.close()
    cs.close()
    cs2.close()
    exit()
