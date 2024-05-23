# -*- coding: utf-8 -*-
"""
Created on Sun May 12 01:12:53 2024

@author: hp
"""
import requests
import os
from cryptography.fernet import Fernet

# Global variable to store the encryption key
encryption_key = b'gTmn5ZDxDxZIzKyMBgTfVU2cK8_uUp4D8mO7L9L84TI='

def list_files():
    url = 'http://localhost:5000/list_files'
    response = requests.get(url)
    data = response.json()
    if 'files' in data:
        print("Available files on server:")
        for file in data['files']:
            print(file)

def download_file(filename):
    url = f'http://localhost:5000/download/{filename}'
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"File '{filename}' downloaded successfully")

        # Decrypt the content of the downloaded file using the encryption key
        cipher_suite = Fernet(encryption_key)
        with open(filename, 'rb') as f:
            encrypted_content = f.read()
        decrypted_content = cipher_suite.decrypt(encrypted_content)

        # Get the path to the downloads_files directory
        downloads_dir = os.path.join(os.path.dirname(__file__), 'downloads_files')
        os.makedirs(downloads_dir, exist_ok=True)

        # Write the decrypted content to a new file
        decrypted_filename = os.path.join(downloads_dir, filename.replace('.enc', ''))
        with open(decrypted_filename, 'wb') as f:
            f.write(decrypted_content)

        print(f"Decrypted content of the file written to '{decrypted_filename}'")

    else:
        print(f"Failed to download file '{filename}'")

def upload_file_original(filename, content, priority):
    cipher_suite = Fernet(encryption_key)
    encrypted_content = cipher_suite.encrypt(content.encode())

    # Save the encrypted content to a temporary file
    encrypted_filename = filename + f"_{priority}" + ".enc"
    with open(encrypted_filename, 'wb') as f:
        f.write(encrypted_content)

    # Continue with file upload to the original server
    url_original = 'http://localhost:5000/upload'
    files = {'file': open(encrypted_filename, 'rb')}
    response_original = requests.post(url_original, files=files)

    if response_original.status_code == 200:
        print(f"File '{filename}' uploaded successfully to original servers")
    else:
        print(f"Failed to upload file '{filename}' to one or original servers")

def upload_file_backup(filename, content, priority):
    cipher_suite = Fernet(encryption_key)
    encrypted_content = cipher_suite.encrypt(content.encode())

    # Save the encrypted content to a temporary file
    encrypted_filename = filename + f"_{priority}" + ".enc"
    with open(encrypted_filename, 'wb') as f:
        f.write(encrypted_content)

    # Continue with file upload to the backup server
    url_backup = 'http://localhost:5001/upload'
    files_backup = {'file': open(encrypted_filename, 'rb')}
    response_backup = requests.post(url_backup, files=files_backup)

    if response_backup.status_code == 200:
        print(f"File '{filename}' uploaded successfully to the backup servers")
    else:
        print(f"Failed to upload file '{filename}' to the backup servers")

if __name__ == '__main__':
    flag = True
    while flag:
        action = input("Do you want to (1) list files, (2) download file, or (3) upload file or (4) quit? ")
        if action == '1':
            list_files()
        elif action == '2':
            filename_to_download = input("Enter the filename you want to download: ")
            if filename_to_download == "":
                print("Invalid file name")
            else:
                download_file(filename_to_download)
        elif action == '3':
            priority_list = ["high","low","medium"]
            filename = input("Enter the filename you want to upload: ")
            content = input("Enter the content of the file: ")
            priority = input("Enter the priority level (low, medium, high): ")
            if filename == "" or content == "" or priority == "" or priority.lower() not in priority_list:
                print("Invalid filename or content or priority")
            else:
                upload_file_original(filename, content, priority)
                upload_file_backup(filename, content, priority)
        elif action == '4':
            flag == False
            print("QUIT!!!")
            break
        else:
            print("Invalid choice")