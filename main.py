# PyFi is a LINUX utility that utilizes a host's wireless NIC to
# scan the local network for adjacent WiFi-utilizing devices

if __name__ == '__main__':
    import socket
    import os
    import sys
    from scapy.all import *
    from threading import Thread
    import pandas
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

        localhost_ip = socket.gethostbyname(localhost)
        print(f"localhost IP address: {localhost_ip}")

        # Function to get the current time and date
        def GetDateTime():
            print(f"Date: {date.today()}")
            now = datetime.now()
            timeNow = now.strftime('%H:%M:%S')
            print(f"Time: {timeNow}")
            print("~" * 40)

        # Probes all WiFi-using devices for pertinent information
        def SniffWifi():
            local_devices = pandas.DataFrame(columns=["BSSID", "SSID", "dBm_Signal", "Channel", "Crypto"])
            local_devices.set_index("BSSID", inplace=True)

            pkt = sniff(count=1, filter="ip")

            # Profiles sniffed network packets based on presence of IEEE 802.11 protocol (WiFi)
            def callback(pkt):
                if pkt[0].haslayer(Dot11Beacon):
                    bssid = packet[Dot11].addr2
                    ssid = packet[Dot11Elt].info.decode()

                    try:
                        dbm_signal = packet.dBm_AntSignal
                    except:
                        dbm_signal = "N/A"
                    stats = packet[Dot11Beacon].network_stats()
                    channel = stats.get("channel")
                    crypto = stats.get("crypto")
                    local_devices.loc[bssid] = (ssid, dbm_signal, channel, crypto)

                # Prints discovered info
                def print_all():
                    while True:
                        os.system("clear")
                        print(local_devices)
                        time.sleep(0.5)

                # Sends prompt to localhost to change WiFi NIC's channel
                def change_channel():
                    ch = 1
                    while True:
                        os.system(f"iwconfig {interface} channel {ch}")
                        ch = ch % 14 + 1
                        time.sleep(0.5)

                interface = sys.argv[1] if len(sys.argv) > 1 else '.'
                printer = Thread(target=print_all)
                printer.daemon = True
                printer.start()
                channel_changer = Thread(target=change_channel)
                channel_changer.daemon = True
                channel_changer.start()
                sniff(prn=callback, iface=interface)

            callback(pkt)

        GetDateTime()
        SniffWifi()

    PyFi()