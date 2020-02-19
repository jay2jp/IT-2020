import threading
import time
import random
import socket as mysoc

class client:
    args = sys.argv
    rsPort = args[2]
    tsPort = args[3]
    tsPort = 0
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))

    def rsHostname(self):

    def rslistenPort(self):

    def tsListenPort(self):
