import os

PASSWORD = "hello"
INDICATOR_FILE = ".encrypted"

def xor_encrypt_decrypt(data, key):
    key = (key * (len(data) // len(key) + 1))[:len(data)]
    return bytes([d ^ ord(k) for d, k in zip(data, key)])

def decrypt_folder(folder_path):
    indicator_path = os.path.join(folder_path, INDICATOR_FILE)
    if not os.path.exists(indicator_path):
        print(f"Files in {folder_path} are not encrypted. Nothing to decrypt.")
        return
    
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            if filename != os.path.basename(__file__):
                try:
                    with open(file_path, 'rb') as file:
                        file_data = file.read()
                    
                    decrypted_data = xor_encrypt_decrypt(file_data, PASSWORD)
                    
                    with open(file_path, 'wb') as file:
                        file.write(decrypted_data)
                    print(f"Decrypted: {file_path}")
                except Exception as e:
                    print(f"Failed to decrypt {file_path}: {e}")

    os.remove(indicator_path)
    print(f"Decryption complete for {folder_path}. Indicator file removed.")

def decrypt_folders():
    pictures_folder = os.path.join(os.path.expanduser('~'), 'Pictures')
    music_folder = os.path.join(os.path.expanduser('~'), 'Music')
    documents_folder = os.path.join(os.path.expanduser('~'), 'Documents')
    

    decrypt_folder(pictures_folder)
    decrypt_folder(music_folder)
    decrypt_folder(documents_folder)

if __name__ == "__main__":
    decrypt_folders()