#Plain Text Encrypter for safe message transmission

from Crypto.Cipher import Blowfish
import binascii

Keydict={1:"1234567812345678",2:"3214567812345678",3:"3456754613980752",4:"7656787656781097"}
ivdict={1:"1234567812345678",2:"3214567812345678",3:"3456754613980752",4:"7656787656781097"}

k=int(input("Enter the number:"))
key_hex = Keydict[k]
key = binascii.unhexlify(key_hex)
iv_hex = ivdict[k]
iv = binascii.unhexlify(iv_hex)


cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
plaintext = input('Enter the plaintext to encrypt: ').encode('utf-8')
plaintext_padded = plaintext + ((8 - len(plaintext) % 8) * b' ')
ciphertext = cipher.encrypt(plaintext_padded)
ciphertext_hex = binascii.hexlify(ciphertext).decode('utf-8')
print('Encrypted ciphertext (in hexadecimal):', ciphertext_hex)