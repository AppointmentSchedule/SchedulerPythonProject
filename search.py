

from geopy.geocoders import Nominatim
from geopy.distance import geodesic
# def perform_search(appointment_type, city_province, priority_number):
#     # Implement your search logic here
#     # For demonstration, we'll just print the values
#     print(f"Appointment Type: {appointment_type}")
#     print(f"City, Province: {city_province}")
#     print(f"Priority Number: {priority_number}")
#
#     # You can add more complex logic here, such as querying a database, etc.
#     # Return the search results or any necessary data
#     return {"result": "search completed"}


# def perform_search(address, appointments):
#     geolocator = Nominatim(user_agent="appointment_locator")
#     location = geolocator.geocode(address)
#
#     if not location:
#         return []
#
#     user_coords = (location.latitude, location.longitude)
#
#     def distance_to_user(appointment):
#         appointment_coords = appointment["coordinates"]
#         return geodesic(user_coords, appointment_coords).kilometers
#
#     sorted_appointments = sorted(appointments, key=distance_to_user)
#
#     return sorted_appointments

import geopy.distance


def perform_search(user_address, appointments):
    print('')
    # Mock coordinates for the user's address
    # user_coordinates = (43.4500, -79.6833)
    #
    # def get_distance(coords1, coords2):
    #     return geopy.distance.distance(coords1, coords2).km
    #
    # sorted_appointments = sorted(appointments, key=lambda appt: get_distance(user_coordinates, appt['coordinates']))
    # return sorted_appointments
