import time
import random

def get_random(length: int, seed_time: int):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(seed_time) # Seed with our time :D
    s = ""
    for i in range(length):
        s += random.choice(alphabet)
    return s

import socket

host = "verbal-sleep.picoctf.net"
port = 62133

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    while True:
        data = s.recv(1024).decode()
        print(data)
        start_time = int(time.time() * 1000)
        possible_tokens = []
        for seed_time in range(start_time - 50, start_time + 50):
            possible_tokens.append(get_random(20, seed_time) + "\n")
        for token in possible_tokens:
            print(token)
            s.send(token.encode())
            data = s.recv(1024).decode()
            print(data)
            # break
