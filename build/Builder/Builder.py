'''
@summary: Crypter Builder: Main
@author: MLS
@version: 0.1
'''

# Import libs
import wx
import json

# Import package modules
from .Gui import Gui
from .Exceptions import *
from .Base import *

###################
## BUILDER CLASS ##
###################
class Builder():
    '''
    @summary: Provides the main Builder object. Controls calls to all other areas
    '''
    
    def __init__(self):
        '''
        @summary: Constructor
        '''
        
        # Load existing config
        try:
            config_dict = self.load_config()
        except ConfigFileNotFound:
            config_dict = {}
        
        # Initialise the Builder GUI
        app = wx.App()
        builder_gui = Gui(self.validate, config_dict)
        builder_gui.Show()
        app.MainLoop()
        
        
    def load_config(self):
        '''
        @summary: Loads the configuration file from disk, if present
        @return: contains of the build config file, or an empty dict
        '''
        
        # Read build config
        try:
            with open(CONFIG_FILE_NAME, "r") as config_file:
                config_dict = json.load(config_file)
        except (IOError, ValueError):
            config_dict = {}
            
        return config_dict
            
        
    def validate(self, config_dict):
        '''
        @summary: Performs configuration validation. 
        @param config_dict: A dict containing the build configuration key value pairs
        @raise ValidationException: If an item fails to validate
        '''
        
        # If config is empty, set to default
        print(config_dict)