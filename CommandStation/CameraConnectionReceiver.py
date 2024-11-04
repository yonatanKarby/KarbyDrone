import cv2
import socket
import struct
import pickle

class CameraConnectionReceiver:
    _connection: socket.socket

    buffer: bytes

    def __init__(self, connection: socket.socket):
        self._connection = connection
        pass

    def Run(self):
        ### new
        data:bytes = bytes()
        payload_size = struct.calcsize("I")
        while True:
            print(f"payload size is: {payload_size}")
            while len(data) < payload_size:
                data += self._connection.recv(4096)
            
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("I", packed_msg_size)[0]
            print(msg_size)

            while len(data) < msg_size:
                data += self._connection.recv(4096)

            frame_data = data[:msg_size]
            data = data[msg_size:]

            print(f"{msg_size}->{len(data)}")
            ###

            frame = pickle.loads(frame_data)
            cv2.imshow("LiveFeed", frame)
            cv2.waitKey(1)