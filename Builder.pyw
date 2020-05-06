'''
@summary: Crypter Build script. Invokes the Crypter Exe Builder
@author: Sithis
'''

# Import libs
import wx
import sys
from CrypterBuilder import Builder

# Process Version
PY_MAJ_VERSION = sys.version_info[0]
PY_MIN_VERSION = sys.version_info[1]

def showErrorDialog(message):
    '''
    Displays an error dialog containing the specified message
    '''

    app = wx.App()
    error_dialog = wx.MessageDialog(None, str(message), "Error", wx.OK | wx.ICON_ERROR)
    error_dialog.ShowModal()
    app.MainLoop()

# Check Version
if PY_MAJ_VERSION != 3 or (PY_MIN_VERSION != 6 and PY_MIN_VERSION != 7):
    showErrorDialog(
        "Python 3.6 or 3.7 is required to use this project. version %s.%s is"
        " not supported" % (PY_MAJ_VERSION, PY_MIN_VERSION)
    )
    sys.exit()

# Open Builder
builder = Builder()
builder.launch()