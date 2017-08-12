'''

@summary: Crypter Exe Builder: Build Thread
@author: MLS
'''

# Import libs
import time
import os
import json
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
        self.__build_stopped = False
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
        self.__console_log(msg="%s input should match regex '%s'. Got '%s'" % (
            BUILDER_CONFIG_ITEMS[input_field]["label"],
            BUILDER_CONFIG_ITEMS[input_field]["regex"].pattern,
            input_value
            ),
            debug_level=3
        )

        # If input matches expected regex, return True
        if not BUILDER_CONFIG_ITEMS[input_field]["regex"].match(input_value):
            raise ValidationException
        # If icon_file, check file exists
        elif input_field == "icon_file" and input_value:
            if not os.path.isfile(input_value):
                raise ValidationException
            else:
                self.__console_log(msg="Icon file at '%s' is a valid file" % input_value, debug_level=3)

        # If field is empty, set it to the defined default value (if there is one, else blank)
        if not input_value and "default" in BUILDER_CONFIG_ITEMS[input_field]:
            return BUILDER_CONFIG_ITEMS[input_field]["default"]

        
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
                self.__build_stopped = True
                break

            # Validate input field
            # If invalid input, log to console and set input field to red
            self.__console_log(msg="Checking %s" % input_field, debug_level=1)
            try:
                # Update field value to default if one set
                default_value = self.validate_input(input_field, self.user_input_dict[input_field])
                if default_value:
                    self.user_input_dict[input_field] = default_value
                    self.__console_log("No value provided for %s. Setting to default '%s'" % (
                        input_field,
                        default_value,
                        ),
                        debug_level=2
                    )
            # Validation failed. Provide field description and expectations
            except ValidationException:
                self.__console_log(
                    msg="Invalid value submitted for '%s'. Expected '%s', such as '%s' but received '%s'" % (
                        BUILDER_CONFIG_ITEMS[input_field]["label"],
                        BUILDER_CONFIG_ITEMS[input_field]["input_requirement"],
                        BUILDER_CONFIG_ITEMS[input_field]["example"],
                        self.user_input_dict[input_field]
                        ),
                    ccode=ERROR_INVALID_DATA,
                    invalid_input_field=input_field
                    )
                self.__in_progress = False
                self.__build_error = True
                break
            
        # Validation success
        if not self.__build_error and not self.__build_stopped:
            self.__console_log(msg="Validation successful", debug_level=1)
            
        # Write runtime config and spec
        self.__create_runtime_config()
        # TODO Perhaps spec should be a separate object.... Actually map this one out with methods
        # Have an add data/resource method, set encryption, write spec, set icon etc. etc.
        
        # TODO Invoke Pyinstaller via subprocess
        
            
        # If not error, set success
        if not self.__build_error and not self.__build_stopped:
            self.__build_success = True
            
        # Build thread finished. Log and Reset build status to prevent further console updates
        self.__in_progress = False
        self.__console_log("Build process thread finished", debug_level=3)
        self.__build_error = False
        self.__build_stopped = False
        self.__build_success = False
        
    
    def __create_runtime_config(self):
        '''
        @summary: Creates and writes ransomware's runtime config file
        '''
        self.__console_log(msg="Creating binary runtime config at %s" % RUNTIME_CONFIG_PATH,
                           debug_level=1)
        config_dict = {}
        
        for config_item in RUNTIME_CONFIG_ITEMS:
            config_dict[config_item] = self.user_input_dict[config_item]
        self.__console_log(msg="Runtime config: %s" % config_dict, debug_level=3)
            
        with open(RUNTIME_CONFIG_PATH, "w") as runtime_config_file:
            json.dump(config_dict, runtime_config_file)
            
        self.__console_log(msg="Runtime config successfully written", debug_level=1)

        
    
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
        
        
    def finished_with_stop(self):
        '''
        @summary: Determines if the build finished because it was halted
        by the user
        @return: True if force halted. False if not force halted
        '''
        if self.__build_stopped:
            return True
        else:
            return False
        

    def stop(self):
        '''
        @summary: To be called to set the stop event and end the build process
        '''
        
        self.__stop_event.set()
        