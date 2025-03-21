from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
import requests
import os
from datetime import datetime

views = Blueprint('views', _name_)
class ActivityRecommendation:
    def __init__(self, temperature, description):
        self.temperature = temperature
        self.description = description.lower() if description else ""
        
    def recommend_activity_based_on_temperature(self):
        # Activity suggestions based on temperature
        if self.temperature > 30:
            return "You can go swimming or head to the beach."
        elif 20 <= self.temperature <= 30:
            return "Perfect for a walk outside, a picnic in the park, or a bike ride."
        elif 10 <= self.temperature < 20:
            return "Great for a beach walk, visiting a café, or taking a scenic drive."
        else:
            return "Stay inside with a warm drink, enjoy indoor activities like reading or watching a movie."
    
    def recommend_activity_based_on_weather(self):
        # Activity suggestions based on weather description
        if "rain" in self.description:
            return "It's raining, make sure to bring an umbrella! Consider indoor activities like visiting a museum, going to the cinema, or shopping."
        elif "snow" in self.description:
            return "It's snowing! You can go skiing, ice skating, or build a snowman."
        elif "clear" in self.description:
            return "Clear skies, it's a great day for outdoor activities! Consider a nature hike, visiting the park, or going for a run."
        elif "cloud" in self.description:
            return "Cloudy weather, a good time to enjoy a relaxed walk or head to a cozy café. You can also try indoor activities like bowling."
        elif "fog" in self.description:
            return "It's foggy, visibility might be low. Consider staying inside and enjoying indoor games or cooking a new recipe."
        elif "storm" in self.description:
            return "Stormy weather, it's best to stay indoors. You can enjoy some indoor hobbies like painting, cooking, or watching movies."
        else:
            return "It's a great day to enjoy indoor or outdoor activities!"
    
    def recommend_activity_based_on_time(self):
        # Get current hour
        current_hour = datetime.now().hour
        
        # Early morning (5-8)
        if 5 <= current_hour < 8:
            return "Early morning is perfect for yoga, meditation, or a morning jog to start your day energized."
        # Morning (8-11)
        elif 8 <= current_hour < 11:
            return "It's mid-morning - a great time to visit a café for breakfast, explore a farmers market, or do some shopping before crowds form."
        # Midday (11-14)
        elif 11 <= current_hour < 14:
            return "It's lunchtime! Find a nice restaurant, enjoy a picnic in the park, or visit a museum during this less crowded time."
        # Afternoon (14-17)
        elif 14 <= current_hour < 17:
            return "Afternoon is ideal for outdoor activities, visiting attractions, or taking a leisurely walk to enjoy the day."
        # Evening (17-20)
        elif 17 <= current_hour < 20:
            return "Early evening is perfect for dinner plans, catching a movie, or enjoying sunset views at a scenic spot."
        # Night (20-23)
        elif 20 <= current_hour < 23:
            return "Nighttime offers opportunities for stargazing, enjoying nightlife, attending an evening show, or having a relaxed dinner."
        # Late night (23-5)
        else:
            return "Late night is best for relaxing activities - reading a book, watching a movie, or getting some rest for tomorrow."


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
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={API_KEY}'# Aktivite önerilerini oluþtur
    recommender = ActivityRecommendation(temp, description)
    temp_activity = recommender.recommend_activity_based_on_temperature()
    weather_activity = recommender.recommend_activity_based_on_weather()
    time_activity = recommender.recommend_activity_based_on_time()
    
    # Þu anki saati de gönder
    current_time = datetime.now().strftime("%H:%M")
    
    return jsonify({
        'city': city,
        'temp': temp,
        'description': description,
        'current_time': current_time,
        'temp_activity': temp_activity,
        'weather_activity': weather_activity,
        'time_activity': time_activity
    })


def get_api_key():
    file_path = "api_key_txt"
    with open(file_path, 'r') as file:
        return file.read().strip()