#!/usr/bin/python3
import sys
import os

class XOR:
    def __init__(self):
        self.key = b''
        if ed == "-e":
            self.key = os.urandom(4)
        elif ed == "-d":
            keyhex = sys.argv[3] #hex
            self.key = bytes.fromhex(keyhex)
        print("Key:", self.key.hex())
    def encrypt(self, data: bytes):
        xored = b''
        for i in range(len(data)):
            xored += bytes([data[i] ^ self.key[i % len(self.key)]])
        return xored
    def decrypt(self, data):
        xored = b''
        for i in range(len(data)):
            xored += bytes([data[i] ^ self.key[i % len(self.key)]])
        regstr = xored.decode('utf-8')
        return regstr

def main():
    global inp
    global ed 

    try:
        ed = sys.argv[1]
        crypto = XOR()
        if ed == "-d":
            inp = bytes.fromhex(sys.argv[2])
            print ('Decrypted:', crypto.encrypt(inp).decode('utf-8'))
        elif ed == "-e":
            inp = sys.argv[2].encode('utf-8')
            print('Encrypted:', crypto.encrypt(inp).hex())
    except:
        print("provide a proper input\nExamples:")
        print(" Encryption\n  python3 xor_crypter -e ABCD")
        print(" Decryption\n  python3 crypt/xor_crypter.py -d e7e22febc0a714e8ddeb27 af874387")

if __name__ == '__main__':
    main()
