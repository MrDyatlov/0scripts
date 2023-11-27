import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == "RansomWare_File.py" or file == "ransomkey.key" or file == "RansomCracker.py":
        continue
    if os.path.isfile(file):
        # Şifrelenmesi için belirtilen yolda, dosyaları ayıkla ve şifrele. Klasörleri şifrelemez.
        files.append(file)


with open("ransomkey.key", "rb") as generatedkey:
    cracker = generatedkey.read()


for file in files:

    with open(file, "rb") as theFile:
        contents = theFile.read()

    decryption = Fernet(cracker).decrypt(contents)

    with open(file, "wb") as theFile:
        theFile.write(decryption)

os.remove("ransomkey.key")