import os
from weather_app import WeatherApp

if __name__ == '__main__':
    api_key = os.environ.get('OPEN_WEATHER_API_KEY')
    weather_app = WeatherApp(api_key)
    weather_app.run()