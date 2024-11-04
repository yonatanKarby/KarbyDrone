import socket
import CameraConnectionReceiver

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 6969
buffer_size = 1024 * 1024

server_adress = ('0.0.0.0', port)
server_socket.bind(server_adress)

server_socket.listen()

while(True):
    connection, client_adress = server_socket.accept()
    print(f"Connection from: {client_adress}")
    handler = CameraConnectionReceiver.CameraConnectionReceiver(connection)
    handler.Run()

server_socket.close()
