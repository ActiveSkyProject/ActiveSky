from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
import requests

views = Blueprint('views', __name__)

@views.route('/')
#login required eklenebilir
def home():
    return render_template("base.html")
    #anasayfa.html eklenebilir

@views.route('/anasayfa')
@login_required
def mainPage():
    return render_template("anasayfa.html", user=current_user)

@views.route('/anasayfa', methods=['POST'])
@login_required
def get_weather():
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']

    API_KEY = get_api_key()
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={API_KEY}'

    response = requests.get(url).json()
    city = response['name']
    temp = response['main']['temp']
    description = response['weather'][0]['description']

    return jsonify({'city': city, 'temp': temp, 'description': description})

def get_api_key():
    file_path = "C:\\Users\\elif4\\ActiveSky\\api_key_txt"
    with open(file_path, 'r') as file:
        return file.read().strip()
