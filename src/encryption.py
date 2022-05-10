from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("src/encryption_keys.key", "wb") as key_file:
        key_file.write(key)

def encrpyt_msg(message):
    key = open("src/encryption_keys.key", "rb").read()
    fernet = Fernet(key)
    enc_message = fernet.encrypt(message.encode())
    return enc_message

def decrypt_msg(message):
    key = open("src/encryption_keys.key", "rb").read()
    fernet = Fernet(key)
    dec_message = fernet.decrypt(message).decode()
    return dec_message
    


