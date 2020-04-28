#!/bin/python

import socket
from time import sleep

def main():
    connfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    connfd.connect(("localhost",9999))

    while True:
        data = "x" * 1024
        connfd.send(data)
        sleep(1)

if __name__ == "__main__":
    main()