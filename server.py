import socket
import threading

#array to store the users 
users = []

#function to handle what to do once new client connects to server
def on_new_client(clientsocket, addr):
    print('Got connection from', addr)
    #while loop to constantly check and recieve if client has sent message
    while True:
        try:
            msg = clientsocket.recv(1024)
            #log message to the server and then send the message to other clients that are connected
            if msg:
                print(f'{addr[0]}:{addr[1]} - {msg.decode()}')
                msg_to_broadcast = f'From {addr[0]}:{addr[1]} - {msg.decode()}'
                broadcast(msg_to_broadcast, clientsocket)
            else:
                remove_connection(clientsocket)
                break
        except Exception as e:
            print(f'Error receiving message: {e}')
            remove_connection(clientsocket)
            break
#function to handle sending message to other connect connected client
def broadcast(message: str, sender_socket: socket.socket):
    #goes through array of users connected and sends it to all users that is not the client that sent that message
    for client_conn in users:
        if client_conn != sender_socket:
            try:
                client_conn.send(message.encode())
            except Exception as e:
                print(f'Error broadcasting message: {e}')
                remove_connection(client_conn)

#function to handle disconencting users
def remove_connection(conn: socket.socket) -> None:
    if conn in users:
        conn.close()
        users.remove(conn)

def main():
    #create socket
    s = socket.socket()
    print("Socket successfully created")
    
    #port that the service will ran on
    port = 1223
    s.bind(('', port))
    print(f"Socket binded to {port}")
    
    #socket listening for connection
    s.listen(5)
    print("Socket is listening")
    
    #accept connections and add user to the array of users and create thread to handlen each new user that connects
    while True:
        c, addr = s.accept()
        users.append(c)
        client_thread = threading.Thread(target=on_new_client, args=(c, addr))
        client_thread.start()

if __name__ == "__main__":
    main()

