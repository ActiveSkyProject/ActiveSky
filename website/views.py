import random
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
import requests
import os
from datetime import datetime

views = Blueprint('views', __name__)
class ActivityRecommendation:
    def __init__(self, temperature, description):
        self.temperature = temperature
        self.description = description.lower() if description else ""
        
    def recommend_activity_based_on_temperature(self):
        # S�cakl��a g�re aktivite �nerileri listesi
        if self.temperature > 30:
            activities = [
                "Y�zmeye gidebilir veya plaja gidebilirsiniz.",
                "Serinlemek i�in su park�na gidebilirsiniz.",
                "Yerel bir d�kk�nda dondurma keyfi yapabilirsiniz.",
                "A��k havada bir kafede serinletici bir i�ecek i�ebilirsiniz.",
                "Yak�ndaki bir g�lde kano veya k�rek s�rf� yapabilirsiniz."
            ]
        elif 20 <= self.temperature <= 30:
            activities = [
                "D��ar�da y�r�y�� yapmak i�in m�kemmel.",
                "Parkta piknik yapabilirsiniz.",
                "Bisiklet s�rebilirsiniz.",
                "A��k hava pazar� veya festivalini ziyaret edebilirsiniz.",
                "Tenis veya voleybol gibi a��k hava sporlar� oynayabilirsiniz."
            ]
        elif 10 <= self.temperature < 20:
            activities = [
                "Sahilde y�r�y�� yapmak i�in harika.",
                "S�cak bir i�ecek i�in bir kafeye gidebilirsiniz.",
                "Do�ada manzaral� bir s�r��e ��kabilirsiniz.",
                "Yak�ndaki bir parkurda y�r�y��e ��kabilirsiniz.",
                "Botanik bah�esi veya a��k hava sergisini ziyaret edebilirsiniz."
            ]
        else:
            activities = [
                "S�cak bir i�ecekle i�eride kalabilirsiniz.",
                "Okumak gibi i� mekan aktivitelerinin tad�n� ��karabilirsiniz.",
                "Film izleyebilir veya dizi maratonu yapabilirsiniz.",
                "Kapal� bir m�ze veya sanat galerisini ziyaret edebilirsiniz.",
                "Evde yeni bir tarif deneyebilirsiniz."
            ]
        
        # Rastgele bir aktivite se�
        return random.choice(activities)
    
    def recommend_activity_based_on_weather(self):
        # Hava durumuna g�re aktivite �nerileri listesi
        if "rain" in self.description:
            activities = [
                "Ya�mur ya��yor, �emsiyenizi almay� unutmay�n! Bir m�zeyi ziyaret etmeyi d���nebilirsiniz.",
                "Sinemaya gitmek i�in m�kemmel bir zaman.",
                "Yerel bir al��veri� merkezinde al��veri� yapabilirsiniz.",
                "Kapal� bir oyun salonunu ziyaret edebilirsiniz.",
                "Yemek kursu alabilir veya evde yeni bir tarif deneyebilirsiniz."
            ]
        elif "snow" in self.description:
            activities = [
                "Kar ya��yor! Kayak yapabilirsiniz.",
                "Yerel bir pistte buz pateni yapabilirsiniz.",
                "Kardan adam yapabilir veya kartopu sava�� yapabilirsiniz.",
                "Yak�ndaki bir tepede k�zak kayabilirsiniz.",
                "Kar manzaral� �irin bir kafede s�cak bir i�ecek i�ebilirsiniz."
            ]
        elif "clear" in self.description:
            activities = [
                "A��k g�ky�z�, do�a y�r�y��� i�in harika bir g�n!",
                "Piknik yapmak i�in parka gidebilirsiniz.",
                "D��ar�da ko�u yapabilirsiniz.",
                "A��k hava foto�raf��l��� deneyebilirsiniz.",
                "Yerel bir �ift�i pazar�n� veya a��k hava al��veri� alan�n� ziyaret edebilirsiniz."
            ]
        elif "cloud" in self.description:
            activities = [
                "Bulutlu hava, rahat bir y�r�y���n tad�n� ��karmak i�in iyi bir zaman.",
                "Kahve veya �ay i�in �irin bir kafeye gidebilirsiniz.",
                "Bowling gibi i� mekan aktivitelerini deneyebilirsiniz.",
                "K�� bah�esi veya sera ziyaret edebilirsiniz.",
                "Bir kitap�� veya k�t�phaneyi ke�fedebilirsiniz."
            ]
        elif "fog" in self.description:
            activities = [
                "Sisli, g�r�� mesafesi d���k olabilir. ��eride kalmay� d���nebilirsiniz.",
                "Masa oyunlar� veya yapbozlar gibi i� mekan oyunlar�n�n tad�n� ��karabilirsiniz.",
                "Yeni bir tarif pi�irebilir veya lezzetli bir �eyler yapabilirsiniz.",
                "Kapal� bir havuz veya spa ziyaret edebilirsiniz.",
                "Okuma veya podcast dinleme zaman� olabilir."
            ]
        elif "storm" in self.description:
            activities = [
                "F�rt�nal� hava, en iyisi kapal� mekanlarda kalmakt�r.",
                "Resim yapmak gibi i� mekan hobilerinin tad�n� ��karabilirsiniz.",
                "Konforlu yemekler pi�irebilir veya tatl�lar yapabilirsiniz.",
                "Film izleyebilir veya yeni bir dizi ba�latabilirsiniz.",
                "Kart veya masa oyunlar�yla bir oyun gecesi d�zenleyebilirsiniz."
            ]
        else:
            activities = [
                "�� veya d�� mekan aktivitelerinin tad�n� ��karmak i�in harika bir g�n!",
                "Daha �nce hi� gitmedi�iniz yerel bir turistik yeri ziyaret etmeyi deneyebilirsiniz.",
                "Yeni bir �ey ��renmek i�in bir kursa kat�labilirsiniz.",
                "Keyifli bir s�r��e ��k�p �evrenizi ke�fedebilirsiniz.",
                "Bir kafe veya restoranda arkada�lar�n�zla bulu�abilirsiniz."
            ]
        
        # Rastgele bir aktivite se�
        return random.choice(activities)
    
    def recommend_activity_based_on_time(self):
        # �u anki saati al
        current_hour = datetime.now().hour
        
        # Saate g�re aktivite �nerileri listesi
        if 5 <= current_hour < 8:
            activities = [
                "Erken sabah yoga veya meditasyon i�in m�kemmeldir.",
                "G�n�n�ze enerjiyle ba�lamak i�in sabah ko�usuna ��kabilirsiniz.",
                "Huzurlu bir g�ndo�umu y�r�y���n�n tad�n� ��karabilirsiniz.",
                "Yerel bir kafede besleyici bir kahvalt� yapabilirsiniz.",
                "V�cudunuzu uyand�rmak i�in biraz esneme egzersizleri yapabilirsiniz."
            ]
        elif 8 <= current_hour < 11:
            activities = [
                "Sabah�n ortas� - kahvalt� i�in bir kafeye gitmek i�in harika bir zaman.",
                "Kalabal�klar olu�madan �nce bir �ift�i pazar�n� ke�fedebilirsiniz.",
                "Ma�azalar daha az kalabal�kken al��veri� yapabilirsiniz.",
                "Sabah ortas� fitness dersine kat�labilirsiniz.",
                "D��ar�s� hala serin iken bir bah�eyi veya park� ziyaret edebilirsiniz."
            ]
        elif 11 <= current_hour < 14:
            activities = [
                "��le yeme�i vakti! G�zel bir restoran bulabilirsiniz.",
                "Parkta pikni�in tad�n� ��karabilirsiniz.",
                "Bu daha az kalabal�k zamanda bir m�zeyi ziyaret edebilirsiniz.",
                "Yemek kursu veya at�lye �al��mas�na kat�labilirsiniz.",
                "Bir arkada��n�zla ��le yeme�i yiyip sohbet edebilirsiniz."
            ]
        elif 14 <= current_hour < 17:
            activities = [
                "��leden sonra a��k hava aktiviteleri i�in idealdir.",
                "Turistik yerleri veya simgeleri ziyaret edebilirsiniz.",
                "G�n�n tad�n� ��karmak i�in keyifli bir y�r�y��e ��kabilirsiniz.",
                "Vitrin al��veri�i yapabilir veya yerel d�kkanlar� gezebilirsiniz.",
                "A��k havada bir kafede kahve veya �ay�n tad�n� ��karabilirsiniz."
            ]
        elif 17 <= current_hour < 20:
            activities = [
                "Erken ak�am saatleri ak�am yeme�i planlar� i�in m�kemmeldir.",
                "Sinemada film izleyebilirsiniz.",
                "Manzaral� bir noktada g�n bat�m� manzaras�n�n tad�n� ��karabilirsiniz.",
                "Ak�am fitness dersine kat�labilirsiniz.",
                "Yerel bir bira evi veya �arap bar�n� ziyaret edebilirsiniz."
            ]
        elif 20 <= current_hour < 23:
            activities = [
                "Gece vakti y�ld�z g�zlemlemek i�in f�rsatlar sunar.",
                "Yerel gece hayat� veya m�zik mekanlar�n�n tad�n� ��karabilirsiniz.",
                "Ak�am g�sterisi veya performansa kat�labilirsiniz.",
                "Bir restoranda rahat bir ak�am yeme�i yiyebilirsiniz.",
                "Gece foto�raf��l��� y�r�y���ne ��kabilirsiniz."
            ]
        else:
            activities = [
                "Ge� gece, kitap okumak gibi rahatlat�c� aktiviteler i�in en iyisidir.",
                "Yatmadan �nce film veya dizi izleyebilirsiniz.",
                "Rahatlama teknikleri veya meditasyon uygulayabilirsiniz.",
                "Yar�nki aktivitelerinizi planlayabilirsiniz.",
                "Yar�n i�in biraz dinlenebilirsiniz."
            ]
        
        # Rastgele bir aktivite se�
        return random.choice(activities)

@views.route('/')
#login required eklenebilir
def home():
    return render_template("base.html")
    #anasayfa.html eklenebilir

@views.route('/anasayfa')
@login_required
def mainPage():
    return render_template("anasayfa.html", user=current_user)

@views.route('/hakk�m�zda')
def hakk�m�zda():
    return render_template("hakk�m�zda.html")

@views.route('/ileti�im')
def ileti�im():
    return render_template("ileti�im.html")

@views.route('/anasayfa', methods=['POST'])
@login_required
def get_weather():
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']

    API_KEY = get_api_key()
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={API_KEY}'# Aktivite  nerilerini olu tur

    response = requests.get(url).json()
    city = response.get('name')
    temp = response.get('main', {}).get('temp')
    description = response.get('weather', [{}])[0].get('description')
    
    # Aktivite �nerilerini olu�tur
    recommender = ActivityRecommendation(temp, description)
    temp_activity = recommender.recommend_activity_based_on_temperature()
    weather_activity = recommender.recommend_activity_based_on_weather()
    time_activity = recommender.recommend_activity_based_on_time()

    #  u anki saati de g nder
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

@views.route('/change_activities', methods=['POST'])
@login_required
def change_activities():
    data = request.get_json()
    temp = data.get('temp')
    description = data.get('description')
    
    # Yeni �nerileri olu�tur
    recommender = ActivityRecommendation(temp, description)
    temp_activity = recommender.recommend_activity_based_on_temperature()
    weather_activity = recommender.recommend_activity_based_on_weather()
    time_activity = recommender.recommend_activity_based_on_time()
    
    return jsonify({
        'temp_activity': temp_activity,
        'weather_activity': weather_activity,
        'time_activity': time_activity
    })


def get_api_key():
    file_path = "api_key.txt"
    with open(file_path, 'r') as file:
        return file.read().strip()