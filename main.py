# Imports psutil, the needed package for the assignment
import subprocess
import psutil

# First function to display requested information to script user
def showOS():
    print()


# Displays system's current logged-in users
def showUsers():
    print("The users currently logged on include:")
    print(psutil.users())

# Displays short list of currently running system processes
def showProcesses():
    for process in psutil.process_iter():
        try:
            pname = process.name()
            pid = process.pid
            print(pname, '***', pid)
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

# Starts Python 3 on running machine
def invokePy():
    pname = 'python.exe'
    psutil.Popen('python')


# Finds Python3 process and kill it
def killPy():
    for process in psutil.process_iter():
        if process.cmdline() == 'python':
            process.terminate()
            break
    else:
        print('Python 3 not found; unable to terminate.')
        psutil.Popen('python')

if __name__ == '__main__':
    showOS()
    showUsers()
    showProcesses()
    invokePy()
    killPy()