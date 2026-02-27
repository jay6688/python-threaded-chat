# PyTerminalChat 💬

A lightweight, multi-client terminal chat room built entirely in Python using raw sockets and multi-threading. 

I built this project to understand the fundamentals of networking, TCP/IP sockets, and concurrent programming.

## ✨ Features
* **Multi-Client Support**: The server can handle an unlimited number of concurrent client connections.
* **Real-time Broadcasting**: The server acts as a network router, instantly echoing messages to all connected clients.
* **Multi-threading**: Utilizes Python's `threading` module to handle sending and receiving messages simultaneously, breaking out of standard top-to-bottom execution and preventing `recv()` deadlocks.
* **Custom Nicknames**: Users are prompted to choose a unique display name upon joining.

## ⚙️ Prerequisites
* Python 3.x (No external libraries required)

## 🚀 How to Run

1. **Start the Server**: 
   Open a terminal and start the server script. It will run in the background and listen for incoming connections.
   ```bash
   python chat_server.py
