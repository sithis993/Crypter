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
            reg = _winreg.OpenKeyEx(_winreg.HKEY_CURRENT_USER, self.DISABLE_KEY_LOCATION)
            disabled = _winreg.QueryValueEx(reg, "DisableTaskMgr")[0]
            _winreg.CloseKey(reg)
            key_exists = True
        except:
            pass
        
        # If key doesn't exist, create it and set to disabled
        if not key_exists:
            reg = _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, 
                                  self.DISABLE_KEY_LOCATION)
            _winreg.SetValueEx(reg, "DisableTaskMgr", 0,  _winreg.REG_DWORD, 0x00000001)
            _winreg.CloseKey(reg)
        # If enabled, disable it
        elif key_exists and not disabled:
            reg = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, 
                                  self.DISABLE_KEY_LOCATION,
                                  0,
                                  _winreg.KEY_SET_VALUE)
            _winreg.SetValueEx(reg, "DisableTaskMgr", 0,  _winreg.REG_DWORD, 0x00000001)
            _winreg.CloseKey(reg)

    
    def enable(self):
        '''
        @summary: Disables Windows Task Manager
        '''
        key_exists = False
        
        # Try to read the key
        try:
            reg = _winreg.OpenKeyEx(_winreg.HKEY_CURRENT_USER, self.DISABLE_KEY_LOCATION)
            disabled = _winreg.QueryValueEx(reg, "DisableTaskMgr")[0]
            _winreg.CloseKey(reg)
            key_exists = True
        except:
            pass
            
        # If key exists and is disabled, enable it
        if key_exists and disabled:
            reg = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, 
                                  self.DISABLE_KEY_LOCATION,
                                  0,
                                  _winreg.KEY_SET_VALUE)
            _winreg.SetValueEx(reg, "DisableTaskMgr", 0,  _winreg.REG_DWORD, 0x00000000)
            _winreg.CloseKey(reg)
                
    
if __name__ == "__main__":
    test = TaskManager()
    test.enable()