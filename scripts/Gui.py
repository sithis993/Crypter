'''
Created on 23 Mar 2017

@author: sithis
'''

# Import libs
import wx

# Import classes

class Gui():
    
    def __init__(self):
        app = wx.App()
        parent = None
        title = "Ransom"
        
        windowClass(parent, title)
        
        
        app.MainLoop()
        
        
class windowClass(wx.Frame):
    
    def __init__(self, parent, title):
        super(windowClass, self).__init__(parent, title=title, size=(1000,600))
        self.Show()

        
        
if __name__ == "__main__":
    go = Gui()