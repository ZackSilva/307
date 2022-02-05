# Imports psutil, the needed package for the assignment
import subprocess
import psutil
import platform

# First function to display requested information to script user
def showOS():
    print("This system's operating system is:")
    if psutil.MACOS == True:
        print(f"MacOS {platform.version()} Release {platform.release()}")
    elif psutil.WINDOWS == True:
        print(f"Microsoft Windows {platform.version()} Release {platform.release()}")
    elif psutil.LINUX == True:
        print(f"Linux {platform.version()} Release {platform.release()}")
    else:
        print("Unknown/atypical")
    print("")

# Displays system's current logged-in users
def showUsers():
    print("The users currently logged on include:")
    print(psutil.users())
    print("")

# Displays a short list of currently running system processes and their IDs
def showProcesses():
    for process in psutil.process_iter():
        try:
            pname = process.name()
            pid = process.pid
            print(pname, '***', pid)
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print("")

# Starts Python 3 on running machine
def invokePy():
    pname = 'python.exe'
    psutil.Popen('python')

# Finds Python3 process and terminates it
def killPy():
    for process in psutil.process_iter():
        if 'python' in process.cmdline():
            process.terminate()
            break
    else:
        print('Python 3 not found; unable to terminate.')
    print("")

if __name__ == '__main__':
    showOS()
    showUsers()
    showProcesses()
    invokePy()
    killPy()