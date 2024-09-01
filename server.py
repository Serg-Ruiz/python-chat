import socket             
import threading

def on_new_client(clientsocket,addr):
    
    print('Got connection from', addr)
 
    while True:
        data = clientsocket.recv(1024)
        print(data.decode('utf-8'))

        if data.decode('utf-8') == 'bye':
            clientsocket.close()
            break
       
# next create a socket object
s = socket.socket()         
print ("Socket successfully created")
 
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 1223              
 
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
 
# put the socket into listening mode 
s.listen(5)     
print ("socket is listening")            
             
# a forever loop until we interrupt it or 
# an error occurs 
while True: 
# Establish connection with client. 
  c, addr = s.accept()     
  threading._start_new_thread(on_new_client, (c,addr))
 

  

