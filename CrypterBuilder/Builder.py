'''
Crypter Builder
@author: Sithis
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
class Builder():
    '''
    Crypter Builder
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
        # Initialise the Builder GUI
        self.__app = wx.App()
        self.__builder_gui = Gui()


    def launch(self):
        '''
        Launches the Builder GUI
        '''


        self.__builder_gui.Show()
        self.__app.MainLoop()
