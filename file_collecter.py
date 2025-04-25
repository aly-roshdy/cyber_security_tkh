import os
import shutil

def collect_files():
    #Ask the user for a folder path

    print("This Script only scans for file properties .txt, .docx, and .jpg")


    #Defining target file extensions
    target_extensions = ['.txt', '.docx', '.jpg']
    found_files = []


    #Loop until a valid directory is entered
    while True:
        try:
            directory_to_scan = input("Enter the full path of the directory you want to scan: ") #Get path from user
            
            if not os.path.isdir(directory_to_scan):
                raise ValueError("Not a valid directory path.")
            
            break  # Exit loop if path is valid

        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again with the correct.\n")

#Creating staging folder to copy found files into
    staging_folder = "staged_files"
    if not os.path.exists(staging_folder):
        os.makedirs(staging_folder)


    #Start scanning
    print("\nScanning...\n")

    for root, dirs, files in os.walk(directory_to_scan):
        for file in files:
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in target_extensions:
                full_path = os.path.join(root, file)
                print(f"Found: {full_path}")

                #Copy files found to staging folder
                try:
                    dest_path = os.path.join(staging_folder, os.path.basename(full_path))
                    shutil.copy2(full_path, dest_path)  #preserve metadata
                    found_files.append(dest_path)
                except Exception as e:
                    print(f"Failed to copy {full_path}: {e}")

    print(f"\nScan complete. {len(found_files)} files copied to '{staging_folder}'.")
    return found_files

if __name__ == "__main__":
    collect_files()



