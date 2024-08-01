import socket
import pickle
from scrypkle import picklificate, unpickle


class Network:
    def __init__(self, deck):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pNum = self.connect()
        self.send(deck)
        #self.p = self.connect()
        #self.p.cards = deck

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return unpickle(self.client)
        except:
            pass

    def send(self, data):
        try:
            #print("Sending:", data)
            self.client.send(picklificate(data))
            return unpickle(self.client)
        except socket.error as e:
            print(e)

    def get(self):
        try:
            return unpickle(self.client)
        except socket.error as e:
            print(e)

    # 1-way send
    def fire(self, data):
        try:
            self.client.send(picklificate(data))
        except socket.error as e:
            print(e)
