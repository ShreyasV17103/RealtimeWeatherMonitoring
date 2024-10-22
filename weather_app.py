import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

#API_KEY = '6e75668b3fa82bc8e3848ad4c729d5b6'  # Replace with your actual API key
#BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather/<city>', methods=['GET'])
def get_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  
    }
    
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "temp": data['main']['temp'],
            "feels_like": data['main']['feels_like'],  
            "pressure": data['main']['pressure'],     
            "humidity": data['main']['humidity'],      
            "visibility": data['visibility'] / 1000,  
            "clouds": data['clouds']['all'],           
            "sunrise": data['sys']['sunrise'],        
            "sunset": data['sys']['sunset'],           
            "wind_speed": data['wind']['speed'],      
            "description": data['weather'][0]['description'],  
            "coord": data['coord']                       
        }
        return jsonify(weather_info)
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
