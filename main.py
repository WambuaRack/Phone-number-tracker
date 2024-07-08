import phonenumbers
from phonenumbers import geocoder, carrier
from geopy.geocoders import Nominatim

def track_phone_number(phone_number):
    # Parse the phone number
    parsed_number = phonenumbers.parse(phone_number)

    # Get the carrier of the phone number
    carrier_name = carrier.name_for_number(parsed_number, 'en')
    
    # Get the general region (country) of the phone number
    region = geocoder.description_for_number(parsed_number, 'en')

    # Use geopy to get more information about the location
    geolocator = Nominatim(user_agent="phone_location_tracker")
    location = geolocator.geocode(region)

    if location:
        return {
            'carrier': carrier_name,
            'region': region,
            'latitude': location.latitude,
            'longitude': location.longitude,
            'address': location.address
        }
    else:
        return {
            'carrier': carrier_name,
            'region': region,
            'latitude': None,
            'longitude': None,
            'address': None
        }

# Example phone number (replace with the actual phone number)
phone_number = "+254727177155"  # Format should include country code
location_info = track_phone_number(phone_number)

print(location_info)
