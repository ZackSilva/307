# This script validates SSL certificate status based on user input and outputs a log file.
# The SSL and socket modules are imported to
import socket
import ssl

# This function reads the domains.txt file provided in the assignment
def ReadInput():
    domains_txt = open(r'C:\Users\zsilv\Downloads\domains.txt', 'r')
    file_contents = domains_txt.read()
    print(file_contents)

if __name__ == '__main__':
    ReadInput()