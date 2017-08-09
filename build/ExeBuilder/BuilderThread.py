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
from .Exceptions import *
from distutils.command.build import build


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
        self.__in_progress = False
        self.__build_error = False
        self.__build_success = False
        self.__console_log(msg="Constructor()", debug_level=3)
        self.__stop_event = Event()
        self.user_input_dict = user_input_dict
        
        
        # Start the thread
        self.__console_log(msg="Starting build thread", debug_level=3)
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
        return "Builder"
    
    
    def __console_log(self, msg=None, debug_level=0, ccode=0, **kwargs):
        '''
        @summary: Private Console logger method. Logs the Builders progress to the GUI Console
        using wx Publisher update
        @param msg: The msg to print to the console
        @param debug_level: The debug level of the message being logged
        '''
        
        # Define update data dict and add any kwarg items
        update_data_dict = {
            "_class": str(self),
            "msg": msg,
            "debug_level": debug_level,
            "ccode": ccode
            }
        for key, value in kwargs.iteritems():
            update_data_dict[key] = value
        
        # Send update data
        Publisher.sendMessage("update", update_data_dict)
        
        
    def validate_input(self, input_field, input_value):
        '''
        @summary: Validates the value of the specified input field
        @raise ValidationException: If validation of the input field fails
        '''

        # If input matches expected regex, return True
        # TODO If a field input is invalid, change font to red
        if not CONFIG_ITEMS[input_field]["regex"].match(input_value):
            raise ValidationException

        
    def run(self):
        '''
        @summary: Performs the build operation
        '''
        self.__in_progress = True
        
        # Starting validation
        self.__console_log(msg="Checking configuration...", debug_level=1)
        
        # Iterate input fields and validate
        for input_field in self.user_input_dict:
            time.sleep(0.1)
            
            # Break if STOP set
            if self.__stop_event.is_set():
                self.__in_progress = False
                self.__console_log(msg="Force stop detected. Halting build", debug_level=0)
                break

            # Validate input field
            # If invalid input, log to console and set input field to red
            self.__console_log(msg="Checking %s" % input_field, debug_level=1)
            try:
                self.validate_input(input_field, self.user_input_dict[input_field])
            except ValidationException:
                self.__console_log(
                    msg="Invalid value submitted for '%s'" % input_field,
                    debug_level=0,
                    ccode=ERROR_INVALID_DATA,
                    invalid_input_field=input_field
                    )
                self.__in_progress = False
                self.__build_error = True
                break
            
        # TODO If all fields are valid, write the new config to the file
            
        # If not error, set success
        if not self.__build_error:
            self.__build_success = True
            
        # Build thread finished. Log and Reset build status to prevent furhter console updates
        self.__in_progress = False
        self.__console_log("Build process thread finished", debug_level=3)
        self.__build_error = False
        self.__build_success = False
                
                
    def finished_with_error(self):
        '''
        @summary: Determines whether the build process finished with an error
        @return: True if finished with an error. False if finished successfully
        '''
        if self.__build_error:
            return True
        else:
            return False
        
    
    def finished_with_success(self):
        '''
        @summary: Determines whether the build process finished successfully
        @return: True if finished successfully. False is finished with an error
        '''
        if self.__build_success:
            return True
        else:
            return False
            

    def stop(self):
        '''
        @summary: To be called to set the stop event and end the build process
        '''
        
        self.__stop_event.set()
        