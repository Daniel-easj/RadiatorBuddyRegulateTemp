class WeatherData:
    def __init__(self, temperature, dt_txt, cloud_percentage, dt_unix):
        self.temperature = temperature
        self.dt_txt = dt_txt
        self.cloud_percentage = cloud_percentage
        self.dt_unix = dt_unix

# Function to initialize WeatherData objects


def create_weatherdata(temperature, dt_txt, cloud_percentage, dt_unix):
    weather_data = WeatherData(temperature, dt_txt, cloud_percentage, dt_unix)
    return weather_data

# Function to display data from WeatherData object in string format


def __str__(self):
    return (f"temperature : {self.temperature}, dt_txt : {self.dt_txt}, cloud % : {self.cloud_percentage}, dt_unix : {self.dt_unix}")
