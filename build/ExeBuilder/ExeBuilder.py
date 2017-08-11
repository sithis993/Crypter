'''
@summary: Crypter Exe Builder: Main
@author: MLS
@todo: Look at moving the build config files to a separate conf/ or etc/ directory
@todo: Run the pyinstaller subprocess
@todo: Look into adding an "open containing folder" button which opens the folder that the ransomware binary was written to
@todo: Additional config items
    @todo: colour picker option for choosing the backgroung colour
    @todo: Specifying the ransomware name (e.g Crypter)
@todo Add ability to load config files, but load a "Buildconfig.default" if one isn't provided. This should be stored
in the ExeBuilder package dir (in a conf/ or etc/)
@todo: Ship with a default/template config file with predefined defaults 
@todo: Future: Migrate Crypter process to read behaviour and appearence options from a bundled config file
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
            
        