
import socket #imports the socket moduule
import threading #enable program to respond to unlimited connections
import configparser #to allow usage of a configuration file

# Function to read the configuration file and get the file path
def read_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config['Server']['beigefilepath']

#Function to search for strings in the specified file, with an error handler
def search_string_in_file(file_path, search_string):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() == search_string:
                    return True
        return False
    except FileNotFoundError:
        return False
    
# Function to handle each client's connection
def handle_client(client_socket, file_path):
    data = client_socket.recv(1024).decode('utf-8').strip()

    if search_string_in_file(file_path, data):
        response = "STRING FOUND"
    else:
        response = "STRING NOT FOUND"

    client_socket.send(response.encode('utf-8'))
    client_socket.close()

def main():
    config_path = 'config.ini'
    file_path = read_config(config_path)

    server_host = '127.0.0.1'  #Lsten for incoming connections on ths address
    server_port = 9999

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen()

    print(f"Server is listening on {server_host}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket, file_path))
        client_handler.start()

if __name__ == "__main__":
    main()