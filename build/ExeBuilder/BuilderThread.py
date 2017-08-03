'''
@summary: Crypter Exe Builder: Build Thread
@author: MLS
'''

# Import libs
import time
from threading import Thread, Event
from wx.lib.pubsub import setuparg1
from wx.lib.pubsub import pub as Publisher


#########################
## BUILDERTHREAD CLASS ##
#########################
class BuilderThread(Thread):
    '''
    @summary: Provides a Thread for running an exe Build
    '''
    
    def __init__(self, user_input_dict):
        '''
        @summary: Constructor. Starts the thread
        @param user_input_dict: The GUI Form user submitted config
        '''
        # TODO Continue with config dict catch
        self.__console_log(msg="Constructor")
        self.__in_progress = False
        self.__stop_event = Event()
        self.user_input_dict = user_input_dict
        
        
        # Start the thread
        self.__console_log(msg="Starting Thread")
        Thread.__init__(self)
        self.start()
        
    
    def is_in_progress(self):
        '''
        @summary: Method to check if the build is in progress
        @return: True if in progress, False if not in progress
        '''
        
        return self.__in_progress


    def __str__(self):
        '''
        @summary: Return Class name for logging purposes
        '''
        return "BuilderThread"
    
    
    def __console_log(self, msg=None):
        '''
        @summary: Private Console logger method. Logs the Builders progress to the GUI Console
        using wx Publisher update
        @param msg: The msg to print to the console
        '''
        
        Publisher.sendMessage("update", {
            "_class": str(self),
            "msg": msg
            }
        )

        
    def run(self):
        '''
        @summary: Performs the build operation
        '''
        self.__in_progress = True
        
        # Run validation
        self.__console_log(msg="Validating user input...")
        #for field in self.user_input_dict:
        while True:
            # If stop event is set, cancel and exit
            if self.__stop_event.is_set():
                self.__console_log(msg="Force stop detected. Halting build")
                break
            else:
                self.__console_log(msg="Running")
                time.sleep(1)
            

            
    def stop(self):
        '''
        @summary: To be called to set the stop event and end the build process
        '''
        
        self.__stop_event.set()
        