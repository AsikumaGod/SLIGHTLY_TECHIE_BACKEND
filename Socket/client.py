import socket

def main():
    server_host = 'localhost'  #servers address to connect to
    server_port = 9999 #host port to connect to

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    message = input("Enter the string to search for: ")
    client_socket.send(message.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {response}")

    client_socket.close()

if __name__ == "__main__":
    main()
