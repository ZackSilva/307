# PySniffer (utility name) displays the current time and analyzes instances of
# localhost ingress and egress packets transmitted on/with common vulnerable ports and services
# (i.e. FTP 21, Telnet 23)
if __name__ == '__main__':
    from scapy.all import *
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
            print("-" * 25)

        # Displays to the user the destination IP, protocol, and basic
        # contents of localhost packets
        def getVulnPackets():
            print(sniff(filter='tcp', count=5))
            print(sniff(prn=lambda x:x.summary(), count=5))
            print()

        # Runs all nested functions
        getDateTime()
        getVulnPackets()

    pySniffer()

