import cv2
import socket

videoFeeder = cv2.VideoCapture(0)

def generate_frames_stream():
    ret, frame = videoFeeder.read()
    if not ret:
        return b'';
    ret, buffer = cv2.imencode('.jpeg', frame)
    frameData = buffer.tobytes()
    return frameData

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.0.0.21', 6969)

try:
    client_socket.connect(server_address)
    message = generate_frames_stream()
    client_socket.sendall(message)
finally:
    client_socket.close()