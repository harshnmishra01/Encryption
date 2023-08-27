#Decrypter for CipherText

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
ciphertext_hex = input('Enter the ciphertext to decrypt (in hexadecimal): ')
ciphertext = binascii.unhexlify(ciphertext_hex)
plaintext_padded = cipher.decrypt(ciphertext)
plaintext = plaintext_padded.rstrip(b' ')
plaintext_str = plaintext.decode('utf-8')

print('Decrypted plaintext:', plaintext_str)
