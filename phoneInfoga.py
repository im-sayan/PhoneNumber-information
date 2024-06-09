import phonenumbers
from phonenumbers import carrier, geocoder
from geopy.geocoders import Nominatim

phone_number = input("Please enter a phone number with country code (e.g., +14155552671):  # replace with your phone number:- ");

# Parse the phone number
parsed_number = phonenumbers.parse(phone_number, "US")

# Print phone number details
print('Phone number:', phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
print('Country:', phonenumbers.region_code_for_country_code(parsed_number.country_code))
print('Carrier:', carrier.name_for_number(parsed_number, 'en'))
print('National number:', phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL))
print('National number (raw):', parsed_number.national_number)
print('Extension:', parsed_number.extension if parsed_number.extension else 'None')
print('Is valid:', phonenumbers.is_valid_number(parsed_number))
print('Is possible:', phonenumbers.is_possible_number(parsed_number))

# Get the location description for the phone number
description = geocoder.description_for_number(parsed_number, 'en')
print('Location description:', description)

# Geocode the location description using Nominatim
geolocator = Nominatim(user_agent="phoneNumberExercises")
location = geolocator.geocode(description)

# Print the latitude and longitude if the location is found
if location:
    print('Latitude:', location.latitude)
    print('Longitude:', location.longitude)
else:
    print('Location not found')
