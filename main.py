# This script validates SSL certificate status based on user input and outputs a log file.
# The socket and ssl modules are imported to validate certificates of domains herein
import socket
import ssl

# This function reads the domains.txt file provided in the assignment and validates
# Each domain's SSL certificate using a 'for' loop which reads each domain as a
# Separate variable
def PyVal():
    print('Welcome to PyVal')
    print('-' * 70)
    filepath = input("Please enter the full file path of the file's location:")
    domains_txt = open(filepath, 'r')
    print('Based on the file inputted, below are the domains to be evaluated:')
    print('-' * 70)
    lines = domains_txt.readlines()
    count = 0
    for line in lines:
        count += 1
        print("Line{}: {}".format(count, line))
        domain = format(count, ".line")
        context = ssl.create_default_context()
        with socket.create_connection(domain, 443) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                print(ssock.version())

if __name__ == '__main__':
    PyVal()