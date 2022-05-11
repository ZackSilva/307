# After research it seems Nominatim does not allow the user to geolocate by IP so instead
# I've demonstrated other geolocation elements
# Imports the pygeoip package to leverage geolocation functions
from geopy.geocoders import Nominatim

# Main function includes all code as it's really quite simple!
def PyLocator():
    print("Welcome to PyLocator.")
    print('*' * 30)
    loc = Nominatim(user_agent="GetLocationdetails")
    getLoc = loc.geocode(input('What is your location? Please enter a city followed by state/region:'))
    print('*' * 30)

    print(f"Address: {getLoc.address}")
    print(f"Latitude: {getLoc.latitude}")
    print(f"Longitude: {getLoc.longitude}")

if __name__ == '__main__':
    PyLocator()