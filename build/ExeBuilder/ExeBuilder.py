'''
@summary: Crypter Exe Builder: Main
@author: MLS
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
        