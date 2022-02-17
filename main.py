# PyPort (utility name) displays the localhost's open ports
if __name__ == '__main__':
    import socket
    # Overarching function that defines localhost (and handles error if not found) for other functions
    def PyPort():
        print("Welcome to PyPort.")
        print("~" * 40)
        try:
            localhost = socket.gethostname()
            print(f"localhost found. Name: {localhost}")
        except socket.error as error:
            print("localhost not found. Error code: " %error)
        # Grabs the localhost's IP address (need to fine tune)
        def get_local_addressing():
            local_ip = (socket.gethostbyname(localhost))
            print(f"Device LAN addressing: {local_ip}")
        # Scans network for all OPEN ports and lists their IP addresses
        print("~" * 40)
        def scan_ports():
            print("Scanning all ports on device:")
            try:
                for port in range(1,65535):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    result = sock.connect_ex((localhost, port))
                    if result == 0:
                        print(f"Port {port}: OPEN".format(port))
                    sock.close()
            except KeyboardInterrupt:
                print("Scanning stopped.")
            except socket.gaierror:
                print("Invalid hostname provided.")
        # Calls nested functions
        get_local_addressing()
        scan_ports()

    # Calls main function to leverage utility
    PyPort()

