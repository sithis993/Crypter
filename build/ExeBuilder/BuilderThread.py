'''
@summary: Crypter Exe Builder: Build Thread
@author: MLS
'''

# Import libs
import time
from threading import Thread, Event
from wx.lib.pubsub import setuparg1
from wx.lib.pubsub import pub as Publisher

# Import package modules
from .Base import *


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
        self.__console_log(msg="Constructor", debug_level=3)
        self.__in_progress = False
        self.__stop_event = Event()
        self.user_input_dict = user_input_dict
        
        
        # Start the thread
        self.__console_log(msg="Starting Thread", debug_level=3)
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
    
    
    def __console_log(self, msg=None, debug_level=0):
        '''
        @summary: Private Console logger method. Logs the Builders progress to the GUI Console
        using wx Publisher update
        @param msg: The msg to print to the console
        @param debug_level: The debug level of the message being logged
        '''
        
        Publisher.sendMessage("update", {
            "_class": str(self),
            "msg": msg,
            "debug_level": debug_level
            }
        )
        
        
    def __is_valid_input(self, input_field, input_value):
        '''
        @summary: Validates the value of the specified input field
        @return: True if input is valid, otherwise False
        @todo: Continue with field validation
        '''

        # If empty, 
        if not ALL_CONFIG_ITEMS[input_field]["regex"].match(input_value):
            self.__console_log(
                msg="Invalid value submitted for '%s'" % input_field,
                debug_level=0
                )
        
        

        
    def run(self):
        '''
        @summary: Performs the build operation
        '''
        self.__in_progress = True
        
        # Starting validation
        self.__console_log(msg="Checking configuration...", debug_level=1)
        
        # Iterate input fields and validate
        for input_field in self.user_input_dict:
            
            # Break if STOP set
            if self.__stop_event.is_set():
                self.__in_progress = False
                self.__console_log(msg="Force stop detected. Halting build", debug_level=0)
                break

            # Validate input field
            self.__console_log(msg="Checking %s" % input_field, debug_level=1)
            self.__is_valid_input(input_field, self.user_input_dict[input_field])
            
        # FINISHED
        self.__in_progress = False
        self.__console_log("Build Complete")
                
                
            

            
    def stop(self):
        '''
        @summary: To be called to set the stop event and end the build process
        '''
        
        self.__stop_event.set()
        