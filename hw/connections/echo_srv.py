import socket

server_socket = socket.socket()
host = '0.0.0.0'
port = 12345
server_socket.bind((host, port))
server_socket.listen()

conn, addr = server_socket.accept()
execute = True
print(f'Connection established with client {addr}')
conn.send(b'I will send back everything you send to me\n')
while execute:
    conn.recv(1024)