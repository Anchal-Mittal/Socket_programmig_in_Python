#FROM SOCKET WE ARE IMPORTING SOCKET AND TWO VARIABLES AF_INET AND SOCK_STREAM
#AF_NET IS USED FOR IPv4
#SOCK_STREAM IS USED FOR TCP PROTOCOL
import socket
#from socket import socket,AF_INET,SOCK_STREAM
import sys

try:
    
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("socket successfully cretaed ")
except socket.error as err :
    print("error in socket creation %s"(err))

#DEFAULT PORT 
PORT =80
try :
    host_name=socket.gethostbyname("www.google.com")

except socket.gaierror:
        print("ERROR IN RESOLVING THE HOST ")
        sys.exit()

address=(host_name,PORT)
sock.connect(address)
print("SOCKET IS CREATED SUCCESFULLY ON PORT %s" %(host_name))

    
                                   
