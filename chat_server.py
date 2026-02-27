import socket
import threading

# 1. Server Setup
host = "127.0.0.1"
port = 5555
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen() # Notice we removed the '1'! It now accepts unlimited connections.

# 2. The Guest Lists
clients = []
nicknames = []

# --- BROADCAST FUNCTION ---
# This sends a message to EVERY single connected client
def broadcast(message):
    for client in clients:
        client.send(message)

# --- INDIVIDUAL CLIENT HANDLER ---
# The server creates one of these threads for EVERY person who joins
def handle_client(client):
    while True:
        try:
            # Receive message from this specific client and broadcast it to everyone
            message = client.recv(1024)
            broadcast(message)
        except:
            # If the client disconnects or an error occurs, remove them
            index = clients.index(client)
            clients.remove(client)
            client.close()
            
            nickname = nicknames[index]
            broadcast(f"[-] {nickname} left the chat!".encode())
            nicknames.remove(nickname)
            break

# --- MAIN SERVER LOOP (ENDLESS WELCOMING) ---
def receive():
    print(f"[*] Server is up and listening on {host}:{port}...")
    while True:
        # 1. Accept new connection
        client, address = server_socket.accept()
        print(f"[+] Connected with {str(address)}")

        # 2. Ask the client for their nickname
        client.send("NICK".encode())
        nickname = client.recv(1024).decode()
        
        # 3. Add them to the guest lists
        nicknames.append(nickname)
        clients.append(client)

        # 4. Announce them to the room
        print(f"[*] Nickname of the new client is {nickname}!")
        broadcast(f"[+] {nickname} joined the chat!\n".encode())
        client.send("[+] Connected to the server!\n".encode())

        # 5. Start a dedicated thread just to listen to this specific client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Start the server's main loop
receive()