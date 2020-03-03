import threading
import time
import random
import sys
import socket as mysoc

class client:

    @staticmethod
    def rsListenPort(line):
        cs.send(line.encode('utf-8'))
        data=cs.recv(100).decode('utf-8')
        if not data[len(data)-1] == 'A':
            return (False,data)
        client.writeToFile(data)
        return (True,None)

    @staticmethod
    def tsListenPort(line):
        cs2.send(line.encode('utf-8'))
        data2=cs2.recv(100).decode('utf-8')
        client.writeToFile(data2)

    @staticmethod
    def writeToFile(line):
        if bool:
            output = open("RESOLVED.txt","a")
        else:
            output = open("RESOLVED.txt","w")
        output.write(line+"\n")
        output.close()

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
    rs_sameas_myaddr = mysoc.gethostbyname(rsHostName)

    rs_binding=(rs_sameas_myaddr,rsPort)
    cs.connect(rs_binding)


    bool = False

    input = open("PROJI-HNS.txt","r")
    lines = input.readlines()
    for line in lines:
        line = line.rstrip("\n")
        tuple = client.rsListenPort(line)
        if not tuple[0]:
            try:
                cs2=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
            except mysoc.error as err:
                print('{} \n'.format("socket open error ",err))
            word = tuple[1].split(' ')
            ts_sameas_myaddr=mysoc.gethostbyname(word[0])
            ts_binding=(ts_sameas_myaddr,tsPort)
            cs2.connect(ts_binding)
            client.tsListenPort(line))
            cs2.close()
        bool = True

    input.close()
    cs.close()
    exit()
