import socket
import threading

# Ask the user for their nickname right away
nickname = input("Choose your nickname: ")

# 1. Client Setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 5555

print(f"[*] Connecting to server...")
client_socket.connect((host, port))

# --- THE BACKGROUND WORKER (EARS) ---
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            
            # If the server asks for the nickname, send it!
            if message == 'NICK':
                client_socket.send(nickname.encode())
            else:
                # Otherwise, just print the message normally
                print(message)
        except:
            print("\n[-] Disconnected from the server.")
            client_socket.close()
            break

# --- START THE THREAD ---
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# --- THE MAIN LOOP (MOUTH) ---
while True:
    # Format the message to include the nickname before sending
    text = input("")
    if text.lower() == 'exit':
        client_socket.close()
        break
        
    message = f"[{nickname}]: {text}"
    client_socket.send(message.encode())