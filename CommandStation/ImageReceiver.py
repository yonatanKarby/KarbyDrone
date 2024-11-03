import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 6969
buffer_size = 1024 * 1024

server_adress = ('0.0.0.0', port)
server_socket.bind(server_adress)

server_socket.listen()

while(True):
    connection, client_adress = server_socket.accept()
    print(f"Connection from: {client_adress}")
    outputFile = open(f"{client_adress[0]}.jpeg", '+bw')

    while True:
        data = connection.recv(buffer_size)
        if not data:
            break
        outputFile.write(data)
    outputFile.close()
    connection.close()

server_socket.close()
