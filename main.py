# This script validates SSL certificate status based on user input and outputs a log file.
# The SSL and socket modules are imported to
import socket
import ssl

# This function reads the domains.txt file provided in the assignment
def ReadInput():
    filepath = input("Please enter the full file path of the file's location:")
    domains_txt = open(filepath, 'r')
    print('Based on the file inputted, below are the domains to be evaluated:')
    print('-' * 70)
    print(domains_txt.read())

    lines = domains_txt.readlines()
    count = 0
    for line in lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))

# To validate active SSL certificates
def EvalInput():
    print()

# This function outputs a log file from the evaluated file_contents variable store
def OutputLog():
    print()

if __name__ == '__main__':
    ReadInput()
    EvalInput()
    OutputLog()