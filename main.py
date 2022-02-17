# PyPort (utility name) displays the localhost's ports, IP address, specific port number,
# and ONLY OPEN port statuses.
if __name__ == '__main__':
    import socket
    import sys
    # Overarching function that defines localhost (and handles error if not found) for other functions
    def PyPort():
        try:
            localhost = socket.gethostname()
            print(f"localhost found. Name: {localhost}")
        except socket.error as error:
            print("localhost not found. Error code: " %error)
        # Grabs the localhost's IP address (need to fine tune)
        def get_local_addressing():
            local_ip = (socket.getaddrinfo(localhost, 80))
            print(f"Device LAN addressing: {local_ip}")
        # Scans network for all OPEN ports and lists their IP addresses
        def scan_ports():
            print()

        # Calls nested functions
        get_local_addressing()
        scan_ports()

    # Calls main function to leverage utility
    PyPort()

