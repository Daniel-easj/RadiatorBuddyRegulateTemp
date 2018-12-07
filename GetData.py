import requests
import json
import PiData

WEATHER_REST_URI = 'https://radiatorbuddy.azurewebsites.net/api/weatherdata'
SENSOR_REST_URI = 'https://radiatorbuddy.azurewebsites.net/api/sensorsdata'
WEATHER_DICT_REST_URI = 'https://radiatorbuddy.azurewebsites.net/api/weatherdata/dict'


# Function to get forecast dictionary
def get_forecast_dictionary():
    weather_api_request = requests.get(WEATHER_DICT_REST_URI)
    weather_api_dict = json.loads(weather_api_request.text)
    weather_api_dict == weather_api_request.json()
    forecast_dictionary = dict()
    forecast_dictionary = weather_api_dict.copy()
    return forecast_dictionary

# Function to create incremented name for each meassurement


def create_new_pi_name():
    base_string = 'reading'
    counter = 1
    name = base_string + str(counter)
    return name

# Function to create a list of all meassurements taken by all sensors


def create_sensor_list():
    sensor_api_request = requests.get(SENSOR_REST_URI)
    sensor_api_list = json.loads(sensor_api_request.text)
    sensor_api_list == sensor_api_request.json()
    pi_sensor_list = list()
    for element in sensor_api_list:
        # Fix inserted "T" in timestamp, remove whitespace from location, round temperature
        time_string_with_T = element['timestamp']
        time_string = time_string_with_T.replace('T', ' ')
        # location_string_with_whitespace = element['location']
        # location_string = location_string_with_whitespace.strip()
        location_string = element['location']

        if location_string.strip() == '':
            location_string = None
        else:
            location_string.strip()
        too_long_temperature = element['temperature']
        temperature_with_2_decimals = round(too_long_temperature, 2)
        # Create PiData object, add to list
        name = create_new_pi_name()
        name = PiData.create_pidata(element['id'], temperature_with_2_decimals,
                                    location_string, element['inDoor'],
                                    time_string)
        pi_sensor_list.append(name)
    return pi_sensor_list


# Test of formatting
sensor_list = create_sensor_list()
print(len(sensor_list))
for element in sensor_list:
    # PiData "ToString()"
    print(PiData.__str__(element))
