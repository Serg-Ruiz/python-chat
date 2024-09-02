import socket
import threading

users = []

def on_new_client(clientsocket, addr):
    print('Got connection from', addr)
    
    while True:
        try:
            msg = clientsocket.recv(1024)
            
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

def broadcast(message: str, sender_socket: socket.socket):
    for client_conn in users:
        if client_conn != sender_socket:
            try:
                client_conn.send(message.encode())
            except Exception as e:
                print(f'Error broadcasting message: {e}')
                remove_connection(client_conn)

def remove_connection(conn: socket.socket) -> None:
    if conn in users:
        conn.close()
        users.remove(conn)

def main():
    s = socket.socket()
    print("Socket successfully created")

    port = 1223
    s.bind(('', port))
    print(f"Socket binded to {port}")

    s.listen(5)
    print("Socket is listening")

    while True:
        c, addr = s.accept()
        users.append(c)
        client_thread = threading.Thread(target=on_new_client, args=(c, addr))
        client_thread.start()

if __name__ == "__main__":
    main()

