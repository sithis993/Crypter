'''
@summary: Provides a Task Manager object
@author: MLS
'''

# Import libs
import winreg


class TaskManager(object):
    '''
    @summary: Provides a Task Manager object for managing Windows Task Manager
    @raise WindowsError: If there are problems creating, accessing, reading or writing keys.
    It isn't the job of this class to catch these errors. To be handled (or not) upstream
    '''
    
    DISABLE_KEY_LOCATION = "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System"


    def __init__(self):
        '''
        @summary: Constructor
        '''
        pass
    
    
    def disable(self):
        '''
        @summary: Disables Windows Task Manager
        '''
        key_exists = False
        

        # Try to read the key
        try:
            reg = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, self.DISABLE_KEY_LOCATION)
            disabled = winreg.QueryValueEx(reg, "DisableTaskMgr")[0]
            winreg.CloseKey(reg)
            key_exists = True
        except:
            pass
        
        # If key doesn't exist, create it and set to disabled
        if not key_exists:
            reg = winreg.CreateKey(winreg.HKEY_CURRENT_USER,
                                  self.DISABLE_KEY_LOCATION)
            winreg.SetValueEx(reg, "DisableTaskMgr", 0,  winreg.REG_DWORD, 0x00000001)
            winreg.CloseKey(reg)
        # If enabled, disable it
        elif key_exists and not disabled:
            reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                  self.DISABLE_KEY_LOCATION,
                                  0,
                                  winreg.KEY_SET_VALUE)
            winreg.SetValueEx(reg, "DisableTaskMgr", 0,  winreg.REG_DWORD, 0x00000001)
            winreg.CloseKey(reg)

    
    def enable(self):
        '''
        @summary: Disables Windows Task Manager
        '''
        key_exists = False
        
        # Try to read the key
        try:
            reg = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, self.DISABLE_KEY_LOCATION)
            disabled = winreg.QueryValueEx(reg, "DisableTaskMgr")[0]
            winreg.CloseKey(reg)
            key_exists = True
        except:
            pass
            
        # If key exists and is disabled, enable it
        if key_exists and disabled:
            reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                  self.DISABLE_KEY_LOCATION,
                                  0,
                                  winreg.KEY_SET_VALUE)
            winreg.SetValueEx(reg, "DisableTaskMgr", 0,  winreg.REG_DWORD, 0x00000000)
            winreg.CloseKey(reg)
                
    
if __name__ == "__main__":
    test = TaskManager()
    test.enable()