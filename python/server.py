#!/bin/python
import socket
import sys

def main():
    sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    sockfd.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,int(sys.argv[1]))
    sockfd.bind(("localhost",9999))
    sockfd.listen(5)
    
    while True:
        fd,connaddr = sockfd.accept()
        while True:
            buf = fd.recv(1024)
            if buf:
                print (buf)
            else:
                fd.close()
                break  


if __name__ == "__main__":
    main()
