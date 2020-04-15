'''
@summary: Crypter Build script. Invokes the Crypter Exe Builder
@author: MLS
@version: 0.1
'''

# Import libs
import win32api
from CrypterBuilder import Builder

builder = Builder()
builder.launch()