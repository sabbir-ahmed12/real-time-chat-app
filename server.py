# Import required modules
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
LISTENER_LIMIT = 5

# Main function
def main():
    # Create socket class instance
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"Running the server at {HOST} on port {PORT}")
    except:
        print(f'Unable to bind to host {HOST} on port {PORT}')

    # Set client limit
    server.listen(LISTENER_LIMIT)

    # Listen to client connections
    while True:
        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")


if __name__ == "__main__":
    main()