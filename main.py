# Imports psutil, the needed package for the assignment, platform, and sys
import psutil
import platform
import sys

# Shows the user all system partitions and their disk utilization
def showDisks():
    print(f"System partitions: {psutil.disk_partitions()}")
    print("Disk utilization: " + psutil.disk_usage("c:\\")

if __name__ == '__main__':
    showDisks()