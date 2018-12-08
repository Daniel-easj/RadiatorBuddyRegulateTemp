import GetData
from datetime import datetime, timedelta

one_day_from_now = datetime.now() + timedelta(hours=24)

pi_data_list = GetData.create_sensor_list()
one_day_forecast_list = GetData.create_forecast_list(one_day_from_now)
optimal_temperature = GetData.fake_optimal_temp()


# Function to regulate temperature


def regulate_temp(forecast, indoor_sensor_data, outdoor_sensor_data, optimal_temperature):
    temperature_to_set = 0
    return temperature_to_set

# regulate_temp(one_day_forecast_list, TODO, TODO, optimal_temperature)
