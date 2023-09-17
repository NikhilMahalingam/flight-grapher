import pandas as pd
import numpy as np
import socket
import time
from threading import Timer

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 6000))
s.listen(5)
print('Server is now running.')

def background_controller():
    clientsocket.send(bytes(message, "utf-8"))
    Timer(5, background_controller).start()

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    background_controller()