# python_chat_app
# 🗨️ Custom TCP Chat Application (Python)

> A simple multithreaded TCP chat app built using Python sockets that allows real-time messaging between multiple clients.

---

## 💡 Features
- Real-time messaging between multiple clients  
- Simple text-based interface (runs entirely in terminal)  
- Uses only Python’s built-in `socket` and `threading` libraries  
- No external dependencies or installations required  
- Works locally or across devices on the same network  

---

## ⚙️ Requirements
- **Python 3.8 or higher**  
- Works on Windows, macOS, or Linux  
- No extra installations needed

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository
Open **Terminal / PowerShell / CMD** and run:
```bash
git clone https://github.com/Pragati5555-phoenix/python_chat_app.git
cd python_chat_app
```
### 2️⃣ Start the Server

In one terminal:
```
 python chat_app.py
```
When prompted:
```
Choose mode:
1. Start server
2. Start client
Enter 1 or 2: 1
```

You’ll see:
```
Server started. Waiting for clients to connect...
```

✅ Keep this terminal open, it acts as your chat server.

### 3️⃣ Start the Client(s)

Open another terminal (you can open several ones):
```
python chat_app.py
```

Choose:
```
Enter 1 or 2: 2


Then enter your nickname (e.g. Pogo, Angel, etc.)
```
You’ll see:
```
Connected to the server!
```

Now type messages, they’ll appear for everyone in real-time 🎉

### 🪄 Tech Stack

Language: Python

Libraries: socket, threading (built-in)

Architecture: Client–Server (TCP)

---
 🎓 Student Project -> Python Socket Programming (TCP Chat App)

---
