'''
@summary: Crypter Exe Builder: Main
@author: MLS
@todo: Create appropriate regex patterns for input validation
    @todo: Solve issue with UTF8/unicode regex matching
@todo: Write config out to file
@todo: Run the pyinstaller subprocess
'''

# Import libs
import wx
import json
import time

# Import package modules
from .Gui import Gui
from .Exceptions import *
from .Base import *

###################
## BUILDER CLASS ##
###################
class ExeBuilder():
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
        builder_gui = Gui(config_dict)
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
            
        