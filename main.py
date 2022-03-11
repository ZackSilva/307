# PyFi is a WINDOWS utility that utilizes a host's wireless NIC to
# scan the local network for adjacent WiFi-utilizing devices
if __name__ == '__main__':
    import socket
    from scapy.all import *
    from datetime import datetime
    from datetime import date

    # Parent function for all subfunctions
    def PyFi():
        print("Welcome to PyFi.")
        print("~" * 40)
        try:
            localhost = socket.gethostname()
            print(f"localhost found. Name: {localhost}")
        except socket.error as error:
            print("localhost not found. Error code: " %error)

        # Function to get the current time and date
        def GetDateTime():
            print(f"Date: {date.today()}")
            now = datetime.now()
            timeNow = now.strftime('%H:%M:%S')
            print(f"Time: {timeNow}")
            print("-" * 25)

        def SniffWifi():
            print()


        GetDateTime()
        SniffWifi()

    PyFi()