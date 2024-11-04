import cv2
import socket
import pickle
import struct

videoFeeder = cv2.VideoCapture(0)

def generate_frames_stream():
    ret, frame = videoFeeder.read()
    if not ret:
        return b'';
    return frame

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.0.0.21', 6969)

try:
    client_socket.connect(server_address)
    while True:
        frame = generate_frames_stream()
        data = pickle.dumps(frame) ### new code
        print(len(data))
        dataLengthAsBytes = struct.pack("I", len(data))
        client_socket.sendall(dataLengthAsBytes+data) ### new code
        print("Sent frame")
finally:
    client_socket.close()