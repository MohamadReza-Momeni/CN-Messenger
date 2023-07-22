import socket
import threading

HOST = 'localhost'
PORT = 5000

nickname = input("Enter your nickname: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.send(nickname.encode())
target = input("Enter the recipient: ")
client_socket.send(target.encode())


def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("An error occurred!")
            client_socket.close()
            break


def write():
    while True:
        message = f"{nickname}: {input('')}"
        client_socket.send(message.encode())


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()