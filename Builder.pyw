'''
@summary: Crypter Build script. Invokes the Crypter Exe Builder
@author: Sithis
'''

# Import libs
import win32api
from CrypterBuilder import Builder

builder = Builder()
builder.launch()