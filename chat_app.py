import socket
import threading

HOST = '127.0.0.1'
PORT = 55555

# ---------- SERVER SIDE ----------
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"✅ Server started on {HOST}:{PORT}")
    clients = []
    nicknames = []

    def broadcast(message, _client=None):
        for client in clients:
            if client != _client:
                try:
                    client.send(message)
                except:
                    pass

    def handle_client(client):
        while True:
            try:
                msg = client.recv(1024)
                if not msg:
                    break
                broadcast(msg, client)
            except:
                if client in clients:
                    index = clients.index(client)
                    client.close()
                    nickname = nicknames[index]
                    broadcast(f"{nickname} left the chat.".encode('utf-8'))
                    nicknames.remove(nickname)
                    clients.remove(client)
                break

    def accept_connections():
        while True:
            client, address = server.accept()
            print(f"Connected with {address}")
            client.send("NICK".encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            nicknames.append(nickname)
            clients.append(client)
            print(f"Nickname: {nickname}")
            broadcast(f"{nickname} joined the chat!".encode('utf-8'))
            client.send("Connected to the server!".encode('utf-8'))
            thread = threading.Thread(target=handle_client, args=(client,))
            thread.start()

    accept_connections()

# ---------- CLIENT SIDE ----------
def start_client():
    nickname = input("Choose your nickname: ")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("❌ Could not connect to server. Make sure the server is running first!")
        return

    stop_threads = False

    def receive():
        nonlocal stop_threads
        while not stop_threads:
            try:
                msg = client.recv(1024).decode('utf-8')
                if msg == 'NICK':
                    client.send(nickname.encode('utf-8'))
                else:
                    print(msg)
            except:
                print("❌ Connection closed.")
                stop_threads = True
                client.close()
                break

    def write():
        while not stop_threads:
            msg = f"{nickname}: {input('')}"
            try:
                client.send(msg.encode('utf-8'))
            except:
                break

    threading.Thread(target=receive, daemon=True).start()
    threading.Thread(target=write, daemon=True).start()

# ---------- MAIN ----------
if __name__ == "__main__":
    print("Choose mode:")
    print("1. Start server")
    print("2. Start client")
    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        start_server()
    elif choice == '2':
        start_client()
    else:
        print("Invalid choice. Please restart the program.")
