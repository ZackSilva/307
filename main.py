# PySniffer (utility name) displays the current time and analyzes instances of
# localhost ingress and egress packets transmitted
from scapy.all import *
from datetime import datetime
from datetime import date

# Displays the current date and time in the console
def getDateTime():
    print(f"Date: {date.today()}")
    now = datetime.now()
    timeNow = now.strftime('%H:%M:%S')
    print(f"Time: {timeNow}")
    print("-" * 25)

# Displays to the user the source destination IP, protocol, and basic
# contents of localhost packets. The "count" variable instances are
# set to 100 by default to avoid flooding the console
def sniffPackets():
    print("Sniffing 100 packets on localhost...")
    print(sniff(filter='tcp', count=100))
    print(sniff(prn=lambda x:x.summary(), count=100))

if __name__ == '__main__':
    # Main function for utility
    def pySniffer():
        print("Welcome to PySniffer")
        print("-" * 25)
        # Runs all nested functions
        getDateTime()
        sniffPackets()
    pySniffer()

