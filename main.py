# Imports the pygeoip package to leverage geolocation functions
import pygeoip
gi = pygeoip.GeoIP('GeoIP.dat')
print("Welcome to PyLocator.")
print('*' * 30)

# Function to ask the user for an IP address for analysis
def getIP(address):
    address = input("Please provide an IP address:")

# Function to leverage the pygeoip package for specific geolocation
def scanIP(address):


if __name__ == '__main__':
    address = None
    getIP(address)
    scanIP(address)

