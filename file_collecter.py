import os

def collect_files():
    #Ask the user for a folder path

    print("This Script only scans for file properties .txt, .docx, and .jpg")


    #Defining target file extensions
    target_extensions = ['.txt', '.docx', '.jpg']
    found_files = []
    log_file_name = "files.log"

    #Loop until a valid directory is entered
    while True:
        try:
            directory_to_scan = input("Enter the full path of the directory you want to scan: ") #Get path from user
            
            if not os.path.isdir(directory_to_scan):
                raise ValueError("Not a valid directory path.")
            
            break  # Exit loop if path is valid

        except ValueError as e:
            print(f"[!] Error: {e}")
            print("Please try again with the correct.\n")

    #Start scanning
    print("\nScanning...\n")

    for root, dirs, files in os.walk(directory_to_scan):
        for file in files:
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in target_extensions:
                full_path = os.path.join(root, file)
                print(full_path)
                found_files.append(full_path)

    #Write results to a log file
    with open(log_file_name, "w") as log_file:
        for file_path in found_files:
            log_file.write(file_path + "\n")

    #Outputs Results
    print("\nScan complete.")
    print(f"Total files found: {len(found_files)}")
    print(f"Results saved to: {log_file_name}")

    return found_files

collect_files()

