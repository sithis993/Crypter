'''
@summary: Crypter Exe Builder: Main
@author: MLS
@todo: Adjust GUI to be a scrollable window for the configuration
@todo: Run the pyinstaller subprocess
@todo: Look into adding an "open containing folder" button which opens the folder that the ransomware binary was written to
@todo: Additional config items
    @todo: colour picker option for choosing the backgroung colour
    @todo: Specifying the ransomware name (e.g Crypter)
@todo Add ability to load config files, but load a "Buildconfig.default" if one isn't provided. This should be stored
in the ExeBuilder package dir (in a conf/ or etc/)
@todo: Ship with a default/template config file with predefined defaults 
@todo: Future: Migrate Crypter process to read behaviour and appearance options from a bundled config file
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
        
        # Initialise the Builder GUI
        app = wx.App()
        builder_gui = Gui()
        builder_gui.Show()
        app.MainLoop()
        