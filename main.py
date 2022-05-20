# This script validates SSL certificate status based on user input and outputs a log file.
# The SSL and socket modules are imported to
import socket
import ssl

# This function reads the domains.txt file provided in the assignment
def ReadInput(file_contents):
    filepath = input("Please enter the full file path of the file's location:")
    domains_txt = open(filepath, 'r')
    file_contents = domains_txt.read()
    print('Based on the file inputted, below are the domains to be evaluated:')
    print('-' * 70)
    print(file_contents)

# This function evaluates the file_contents variable in the previous function
# To validate active SSL certificates
def EvalInput(file_contents):
    print()


if __name__ == '__main__':
    file_contents = None
    ReadInput(file_contents)
    EvalInput(file_contents)