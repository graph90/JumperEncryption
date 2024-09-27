# JumperEncryption

## Overview
**JumperEncryption** is a fun project that encrypts files in randomly selected folders using XOR encryption. It moves itself across directories and leaves a note on the desktop once the files have been processed.

## Features
- Encrypts files in the **Pictures**, **Music**, and **Documents** folders.
- Uses XOR encryption with a predefined password.
- Moves the script to a new directory after processing.
- Creates a note on the desktop after encryption.
- Decrypt functionality included to restore encrypted files.

## How it Works
1. The program picks three folders from the user's home directory (Pictures, Music, Documents) at random.
2. It encrypts all files in these folders, skipping over the script itself.
3. The script then moves itself to one of the encrypted folders and relaunches.
4. A note is left on the desktop with a simple message ("hello world").

## Decryption
The repository includes a decryption script to reverse the encryption process. It decrypts files in the **Pictures**, **Music**, and **Documents** folders, restoring them to their original state.

## Usage

1. **Encryption**:  
   Run the `jumper.py` script to encrypt random folders.
2. **Decryption**:
   Run the `undo.py` script to decrypt the folders

Tested on Ubuntu
