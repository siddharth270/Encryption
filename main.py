# String Encryption using python

# Terminal : pip install cryptography
from cryptography.fernet import Fernet

key = Fernet.generate_key()

crypter = Fernet(key)

pw = crypter.encrypt(b'MLHLHD2021Rocks')
decrypter = crypter.decrypt(pw)

print("This is your password: " + str(decrypter,'utf8'))
print("\n This is the encryption of that password: ")
print(str(pw,'utf8'))

