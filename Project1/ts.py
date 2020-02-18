import threading
import time
import random
import socket

class ts:
    def tsListenPort(self):
        dnsTable = {'hostName': '', 'IPadress': socket.gethostbyname(socket.gethostname()), 'flag': ''}

