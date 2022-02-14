# THIS SCRIPT IS MEANT FOR THE WINDOWS 10 OS
# Imports psutil, the needed package for the assignment, and python-diskpart
import psutil
# from python-diskpart import diskpart

# Shows the user all system partitions and their disk utilization
def showDisks():
    print("--------------------------------------")
    print("System partitions:")
    print(psutil.disk_partitions())
    print("Disk utilization in bytes: ")
    print(psutil.disk_usage("/").total)
    print("--------------------------------------")

# Displays system memory statistics to the user
def showMemory():
    print(f"Total system memory installed : {psutil.virtual_memory().total} bytes")
    print(f"Total system memory usage     : {psutil.virtual_memory().used} bytes")
    print(f"Total system memory available : {psutil.virtual_memory().available} bytes")
    print("--------------------------------------")

# (pretends to) creates a new partition on the system and displays to user, then deletes it
def manipulatePartition():
    print("Creating new system partition:")
    # diskpart.createPartition(5)
    print(psutil.disk_partitions())
    drive_letter = 'E'
    print(f"New partition {drive_letter}: created.")
    # diskpart.deletePartition(5)
    print(f"partition {drive_letter}: deleted.")
    print(psutil.disk_partitions())

if __name__ == '__main__':
    showDisks()
    showMemory()
    manipulatePartition()