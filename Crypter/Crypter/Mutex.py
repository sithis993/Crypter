'''
Crypter - Mutext Class
@author: Sithis
'''

# Import Libs
import win32event
import win32api
import winerror

# Import Package Libs

# ================================================================
# = Mutex Class
# ===============================================================
class Mutex():
    '''
    Provides a Mutex object
    '''

    # Properties
    MUTEX_NAME = "mutex_rr_windows"

    def __init__(self):
        '''
        Constructor
        '''
        self.__mutex = self.__acquire()


    def __acquire(self):
        '''
        Attempts to acquire the mutex
        @raise MutexAlreadyAcquired
        '''

        mutex = win32event.CreateMutex(None, 1, self.MUTEX_NAME)
        if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
            raise MutexAlreadyAcquired()

        return mutex


# ================================================================
# = MutexAlreadyAcquired Exception Class
# ===============================================================
class MutexAlreadyAcquired(Exception):
    '''
    To be raised in the even that the mutex has already been acquired
    '''



