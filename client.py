import socket
import sys
import threading

#function to recieve messages from the server
def receive_messages(client_socket):
    while True:
        try:
            #recieve messaage decode it and print it out to the user
            received_msg = client_socket.recv(1024).decode()
            if received_msg:
                print(f"\n{received_msg}")  # Ensure messages are on a new line
            else:
                # Connection closed
                print("\nConnection closed by server")
                break
        except Exception as e:
            print(f"\nError receiving message: {e}")
            break
    #when done closes the socket
    client_socket.close()

def main():
    #tries to create socket if fails error code is thrown ot
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")
    except socket.error as err:
        print(f"Socket creation failed with error {err}")
        sys.exit()
    #port that the service will be run on and ip of the server
    port = 
    host_ip = ''
    #connect to socket on server if it does not suceed throws out error
    try:
        client_socket.connect((host_ip, port))
        print("The socket has successfully connected to the server")
    except socket.error as err:
        print(f"Error connecting to the server: {err}")
        sys.exit()

    # Start a thread to listen for incoming messages
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
    #while loop to constantly ask user for input and see if user wants to disconnect
    while True:
        try:
            user_input = input(">>")
            if user_input.lower() == 'bye':
                client_socket.sendall(user_input.encode('utf-8'))
                print("Disconnecting...")
                break
            client_socket.sendall(user_input.encode('utf-8'))
        except KeyboardInterrupt:
            print("\nInterrupt received, disconnecting...")
            break
        except Exception as e:
            print(f"\nError sending message: {e}")
            break

    client_socket.close()

if __name__ == "__main__":
    main()

