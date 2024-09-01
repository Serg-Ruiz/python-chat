import socket # for socket 
import sys 
 
try: 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print ("Socket successfully created")
except socket.error as err: 
    print ("socket creation failed with error %s" %(err))
 
# default port for socket 
port = 1223 
  
try: 
    host_ip = '50.76.70.60'
except socket.gaierror: 
 
    # this means could not resolve the host 
    print ("there was an error resolving the host")
    sys.exit() 
 
# connecting to the server 
client_socket.connect((host_ip, port)) 

print ("the socket has successfully connected to server")

while True:

    user_input = input("Enter something: ")
    client_socket.sendall(user_input.encode('utf-8'))

    if user_input == 'bye':
        break


