# Part 1: UDP Client
import socket
import random
import math
from time import time

def main():
    serverAddress = ('127.0.0.1', 7777)




    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket.settimeout(5)
    #Make empty counters for both packets sent and lost
    counterLoss=0
    counterSent=0

    rttList=[]



    while counterSent <= 10:
        #Record initial time
        current= time()
        msg= str((counterSent,current))
        clientSocket.sendto(msg.encode(), serverAddress)
        t1 = time()
        #Increment counterSent by 1 for each packet sent
        counterSent+=1
        try:
            (response, address) = clientSocket.recvfrom(1024)
            t2 = time()
            rtt = t2 - t1
            rttList.append(rtt)
        except socket.timeout:
            counterLoss+=1
    #calculate Average round trip time
    avgrtt= sum(rttList)/len(rttList)
    print(rttList)
    #calculate number of packets lost
    packetLoss= counterLoss/counterSent
    print(packetLoss)

main()
