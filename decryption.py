from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import zipfile
import os
print("Saving to:", os.getcwd())

def run_decryption():
    # Load encrypted AES key and decrypt it
    with open("private_key.pem", "rb") as f:
        private_key = RSA.import_key(f.read())

    with open("key_encrypted.bin", "rb") as f:
        encrypted_key = f.read()

    aes_key = PKCS1_OAEP.new(private_key).decrypt(encrypted_key)

    # Load IV
    with open("iv.key", "rb") as f:
        iv = f.read()

    #Decrypt files.log (encrypted zip)
    with open("files.log", "rb") as f:
        encrypted_data = f.read()

    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    data = cipher.decrypt(encrypted_data)
    print("Decrypted data size:", len(data))
    # Remove padding
    data = data[:-data[-1]]

    #Save decrypted zip
    with open("restored.zip", "wb") as f:
        f.write(data)

    #Extract files from zip
    with zipfile.ZipFile("restored.zip", "r") as zipf:
        zipf.extractall("restored_files")

print(f"Current working directory: {os.getcwd()}")
print("Contents of this folder:")
print(os.listdir())


print("\nDecryption complete.")
print("Decrypted zip saved to: restored.zip")
print("Files extracted to folder: restored_files")

if __name__ == "__main__":
    run_decryption()

