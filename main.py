# Imports psutil, the needed package for the assignment
import subprocess
import psutil
import os
import platform

# First function to display requested information to script user
def showOS():
    # Since os.uname doesn't work on Windows, the function will detect an error and except it
    # by instead running the platform module
    print("The operating system of this machine is:")
    while True:
        try:
            print(os.uname())
            break
        except AttributeError:
            print(platform.system() + platform.release())
            break

# Displays system's current logged-in users
def showUsers():
    print("The users currently logged on include:")
    print(psutil.users())

# Displays short list of currently running system processes
def showProcesses():
    print()

# Starts Python 3 on running machine
def invokePy():
    psutil.Process().nice(psutil.ABOVE_NORMAL_PRIORITY_CLASS)
    p = subprocess.Popen


# Uses regex to find Python3 process and kill it
def killPy():
    print()

if __name__ == '__main__':
    showOS()
    showUsers()
    showProcesses()
    killPy()