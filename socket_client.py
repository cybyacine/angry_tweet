import socket
import time

PORT = 5050
SERVER = "192.168.76.140"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    answer = input('Would you like to connect (yes/no)? ')
    if answer.lower() != 'yes':
        return

    connection = connect()

    while True:
        sent_msg = input("Message (q for quit): ")
        if sent_msg == 'q':
            break
        send(connection, sent_msg)
        recv_msg = connection.recv(1024).decode(FORMAT)
        print(recv_msg)

    send(connection, DISCONNECT_MESSAGE)
    time.sleep(1)
    print('Disconnected')
