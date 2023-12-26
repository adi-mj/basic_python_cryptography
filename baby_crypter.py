#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256) #encryption core
    return bytes(ct)

def decryption(msg):
    ct = []
    for char in msg: #decryption
        char = char - 18
        char = char * 179 #modular multiplicative inverse of 123
        char = char % 256
        ct.append(char)
    return bytes(ct)

try:
    ed=sys.argv[1]
    if ed == "-d":
        inp = bytes.fromhex(sys.argv[2])
        oup = decryption(inp)
        print(oup.decode('utf-8'))
    elif ed=="-e":
        inp = sys.argv[2].encode('utf-8')
        oup = encryption(inp)
        print(oup.hex())
except:
    print("provide a proper input\nExamples:")
    print(" Encryption\n  python3 baby_crypter -e ABCD")
    print(" Decryption\n  python3 baby_crypter -d 4dc843be")