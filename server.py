# Import required modules
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
LISTENER_LIMIT = 5
active_clients = []

# Function to keep listen for upcoming messages from a client
def listen_for_messages(client, username):
    while True:
        message = client.recv(2048).decode('utf-8')

        if message != '':
            final_msg = username + '->' + message
            send_message_to_all(final_msg)
        else:
            print(f"An empty message received from {username}.")

# Function to send message to a single client
def send_message_to_client(client, message):
    client.sendall(message.encode())

# Function to send any message to all currently connected client
def send_message_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)

# Function to handle client
def client_handler(client):
    while True:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            break
        else:
            print('Client username is empty')
    threading.Thread(target=listen_for_messages, args=(client, username, )).start()
    
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

        threading.Thread(target=client_handler, args=(client, )).start()


if __name__ == "__main__":
    main()