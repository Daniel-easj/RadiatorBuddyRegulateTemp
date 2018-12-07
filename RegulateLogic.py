import GetData

pi_data_list = GetData.create_sensor_list()
forecast_dictionary = GetData.get_forecast_dictionary()
optimal_temperature = GetData.fake_optimal_temp()

for key, value in forecast_dictionary.items():
    print(key, value)
# for key in forecast_dictionary:
#     if key =

# Function to regulate temperature


def regulate_temp(one_day_forecast, indoor_sensor_data, outdoor_sensor_data, optimal_temperature):
    temperature_to_set = 0
    return temperature_to_set

# regulate_temp(test, test, test, optimal_temperature)
