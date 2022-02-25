# PySniffer (utility name) displays the current time and analyzes instances of
# packets transmitted on/with common vulnerable ports and services (i.e. Telnet, FTP)
if __name__ == '__main__':
    import scapy
    from datetime import datetime
    from datetime import date
    # Main function for utility
    def pySniffer():

        # Displays the current date and time in the console
        def getDateTime():
            print(f"Date: {date.today()}")
            now = datetime.now()
            timeNow = now.strftime('%H:%M:%S')
            print(f"Time: {timeNow}")
        # Runs all nested functions
        getDateTime()

    pySniffer()

