# Imports psutil, the needed package for the assignment, platform, and sys
import psutil
import platform
import sys

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
        print("Unknown")
    print("")

# Displays system's current logged-in users
def showUsers():
    print("The users currently logged on include:")
    print(psutil.users())
    print("")

# Displays a short list of currently running web browser processes and their PIDs
# A nested function is implemented to avoid redundant code in the "if, elif" sequence below
def showProcesses():
    print('Open web browser process(es):')
    for process in psutil.process_iter():
        pname = process.name()
        pid = process.pid
        def findBrowserProcess():
            try:
                print(pname, '***', pid)
            except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        if 'chrome' in pname:
            findBrowserProcess()
        elif 'firefox' in pname:
            findBrowserProcess()
        elif 'internet explorer' in pname:
            findBrowserProcess()
        elif 'opera' in pname:
            findBrowserProcess()
        elif 'edge' in pname:
            findBrowserProcess()
    print("")

# Starts Python 3 on running machine
def invokePy():
    for process in psutil.process_iter():
        pname = process.name()
        if 'python' in pname:
            pass
        elif psutil.WINDOWS == True:
            psutil.Popen('python.exe')
        else:
            locate_python = sys.exec_prefix
            psutil.Popen(locate_python)

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