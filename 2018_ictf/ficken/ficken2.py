from pwn import *

#conn = remote('127.0.0.1', 20001)
#
#print conn.recv()
#data = conn.recv()
#data += conn.recv()
#print data
#conn.send(data)
#print conn.recv()
#conn.close()
#sh = process('/bin/sh')
#sh.sendline('sleep 3; echo "hello world"')
#sh.recvline(timeout=1)
#sh.recvline(timeout=5)
#sh.interactive() 
binary = ELF("/home/ctf/babymarv_orig/src/babymarvel-hex")
r = process("/home/ctf/babymarv_orig/src/babymarvel-hex")
print r.recvline()
print r.recvline()
print r.recvline()
data = r.recvline()
r.sendline(data)
print r.recvline()
print r.recv()
r.sendline("0\r\n")
#print r.recvline()
#r.sendline("myuser\r\n")
#print r.recvline()
#r.sendline("mypassword\r\n")
print r.recvline()
#r.sendline("myuser")
#print r.recvline()
#r.sendline("mypassword")
#print r.recvline()
r.close()
#sh.close()
