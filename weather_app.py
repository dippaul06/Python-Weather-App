from flask import Flask, render_template, request
from weather_fetcher import WeatherFetcher

class WeatherApp:
    def __init__(self, api_key):
        self.app = Flask(__name__, template_folder='template')
        self.weather_fetcher = WeatherFetcher(api_key)
        self.app.add_url_rule('/', view_func=self.index, methods=['GET'])
        self.app.add_url_rule('/weather', view_func=self.weather, methods=['POST'])

    def index(self):
        return render_template('index.html')
    
    def weather(self):
        city = request.form['city']
        weather_data = self.weather_fetcher.get_weather(city)

        if weather_data['cod'] == '404':
            return render_template('weather.html', error='City not found')
        
        else:
            weather_info = {
                'city': city,
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description']
            }
            return render_template('weather.html', weather=weather_info)
        
    def run(self):
        self.app.run(debug=True)
