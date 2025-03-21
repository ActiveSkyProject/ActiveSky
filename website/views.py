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
        # Sıcaklığa göre aktivite önerileri listesi
        if self.temperature > 30:
            activities = [
                "Yüzmeye gidebilir veya plaja gidebilirsiniz.",
                "Serinlemek için su parkına gidebilirsiniz.",
                "Yerel bir dükkânda dondurma keyfi yapabilirsiniz.",
                "Açık havada bir kafede serinletici bir içecek içebilirsiniz.",
                "Yakındaki bir gölde kano veya kürek sörfü yapabilirsiniz."
            ]
        elif 20 <= self.temperature <= 30:
            activities = [
                "Dışarıda yürüyüş yapmak için mükemmel.",
                "Parkta piknik yapabilirsiniz.",
                "Bisiklet sürebilirsiniz.",
                "Açık hava pazarı veya festivalini ziyaret edebilirsiniz.",
                "Tenis veya voleybol gibi açık hava sporları oynayabilirsiniz."
            ]
        elif 10 <= self.temperature < 20:
            activities = [
                "Sahilde yürüyüş yapmak için harika.",
                "Sıcak bir içecek için bir kafeye gidebilirsiniz.",
                "Doğada manzaralı bir sürüşe çıkabilirsiniz.",
                "Yakındaki bir parkurda yürüyüşe çıkabilirsiniz.",
                "Botanik bahçesi veya açık hava sergisini ziyaret edebilirsiniz."
            ]
        else:
            activities = [
                "Sıcak bir içecekle içeride kalabilirsiniz.",
                "Okumak gibi iç mekan aktivitelerinin tadını çıkarabilirsiniz.",
                "Film izleyebilir veya dizi maratonu yapabilirsiniz.",
                "Kapalı bir müze veya sanat galerisini ziyaret edebilirsiniz.",
                "Evde yeni bir tarif deneyebilirsiniz."
            ]
        
        # Rastgele bir aktivite seç
        return random.choice(activities)
    
    def recommend_activity_based_on_weather(self):
        # Hava durumuna göre aktivite önerileri listesi
        if "rain" in self.description:
            activities = [
                "Yağmur yağıyor, şemsiyenizi almayı unutmayın! Bir müzeyi ziyaret etmeyi düşünebilirsiniz.",
                "Sinemaya gitmek için mükemmel bir zaman.",
                "Yerel bir alışveriş merkezinde alışveriş yapabilirsiniz.",
                "Kapalı bir oyun salonunu ziyaret edebilirsiniz.",
                "Yemek kursu alabilir veya evde yeni bir tarif deneyebilirsiniz."
            ]
        elif "snow" in self.description:
            activities = [
                "Kar yağıyor! Kayak yapabilirsiniz.",
                "Yerel bir pistte buz pateni yapabilirsiniz.",
                "Kardan adam yapabilir veya kartopu savaşı yapabilirsiniz.",
                "Yakındaki bir tepede kızak kayabilirsiniz.",
                "Kar manzaralı şirin bir kafede sıcak bir içecek içebilirsiniz."
            ]
        elif "clear" in self.description:
            activities = [
                "Açık gökyüzü, doğa yürüyüşü için harika bir gün!",
                "Piknik yapmak için parka gidebilirsiniz.",
                "Dışarıda koşu yapabilirsiniz.",
                "Açık hava fotoğrafçılığı deneyebilirsiniz.",
                "Yerel bir çiftçi pazarını veya açık hava alışveriş alanını ziyaret edebilirsiniz."
            ]
        elif "cloud" in self.description:
            activities = [
                "Bulutlu hava, rahat bir yürüyüşün tadını çıkarmak için iyi bir zaman.",
                "Kahve veya çay için şirin bir kafeye gidebilirsiniz.",
                "Bowling gibi iç mekan aktivitelerini deneyebilirsiniz.",
                "Kış bahçesi veya sera ziyaret edebilirsiniz.",
                "Bir kitapçı veya kütüphaneyi keşfedebilirsiniz."
            ]
        elif "fog" in self.description:
            activities = [
                "Sisli, görüş mesafesi düşük olabilir. İçeride kalmayı düşünebilirsiniz.",
                "Masa oyunları veya yapbozlar gibi iç mekan oyunlarının tadını çıkarabilirsiniz.",
                "Yeni bir tarif pişirebilir veya lezzetli bir şeyler yapabilirsiniz.",
                "Kapalı bir havuz veya spa ziyaret edebilirsiniz.",
                "Okuma veya podcast dinleme zamanı olabilir."
            ]
        elif "storm" in self.description:
            activities = [
                "Fırtınalı hava, en iyisi kapalı mekanlarda kalmaktır.",
                "Resim yapmak gibi iç mekan hobilerinin tadını çıkarabilirsiniz.",
                "Konforlu yemekler pişirebilir veya tatlılar yapabilirsiniz.",
                "Film izleyebilir veya yeni bir dizi başlatabilirsiniz.",
                "Kart veya masa oyunlarıyla bir oyun gecesi düzenleyebilirsiniz."
            ]
        else:
            activities = [
                "İç veya dış mekan aktivitelerinin tadını çıkarmak için harika bir gün!",
                "Daha önce hiç gitmediğiniz yerel bir turistik yeri ziyaret etmeyi deneyebilirsiniz.",
                "Yeni bir şey öğrenmek için bir kursa katılabilirsiniz.",
                "Keyifli bir sürüşe çıkıp çevrenizi keşfedebilirsiniz.",
                "Bir kafe veya restoranda arkadaşlarınızla buluşabilirsiniz."
            ]
        
        # Rastgele bir aktivite seç
        return random.choice(activities)
    
    def recommend_activity_based_on_time(self):
        # Şu anki saati al
        current_hour = datetime.now().hour
        
        # Saate göre aktivite önerileri listesi
        if 5 <= current_hour < 8:
            activities = [
                "Erken sabah yoga veya meditasyon için mükemmeldir.",
                "Gününüze enerjiyle başlamak için sabah koşusuna çıkabilirsiniz.",
                "Huzurlu bir gündoğumu yürüyüşünün tadını çıkarabilirsiniz.",
                "Yerel bir kafede besleyici bir kahvaltı yapabilirsiniz.",
                "Vücudunuzu uyandırmak için biraz esneme egzersizleri yapabilirsiniz."
            ]
        elif 8 <= current_hour < 11:
            activities = [
                "Sabahın ortası - kahvaltı için bir kafeye gitmek için harika bir zaman.",
                "Kalabalıklar oluşmadan önce bir çiftçi pazarını keşfedebilirsiniz.",
                "Mağazalar daha az kalabalıkken alışveriş yapabilirsiniz.",
                "Sabah ortası fitness dersine katılabilirsiniz.",
                "Dışarısı hala serin iken bir bahçeyi veya parkı ziyaret edebilirsiniz."
            ]
        elif 11 <= current_hour < 14:
            activities = [
                "Öğle yemeği vakti! Güzel bir restoran bulabilirsiniz.",
                "Parkta pikniğin tadını çıkarabilirsiniz.",
                "Bu daha az kalabalık zamanda bir müzeyi ziyaret edebilirsiniz.",
                "Yemek kursu veya atölye çalışmasına katılabilirsiniz.",
                "Bir arkadaşınızla öğle yemeği yiyip sohbet edebilirsiniz."
            ]
        elif 14 <= current_hour < 17:
            activities = [
                "Öğleden sonra açık hava aktiviteleri için idealdir.",
                "Turistik yerleri veya simgeleri ziyaret edebilirsiniz.",
                "Günün tadını çıkarmak için keyifli bir yürüyüşe çıkabilirsiniz.",
                "Vitrin alışverişi yapabilir veya yerel dükkanları gezebilirsiniz.",
                "Açık havada bir kafede kahve veya çayın tadını çıkarabilirsiniz."
            ]
        elif 17 <= current_hour < 20:
            activities = [
                "Erken akşam saatleri akşam yemeği planları için mükemmeldir.",
                "Sinemada film izleyebilirsiniz.",
                "Manzaralı bir noktada gün batımı manzarasının tadını çıkarabilirsiniz.",
                "Akşam fitness dersine katılabilirsiniz.",
                "Yerel bir bira evi veya şarap barını ziyaret edebilirsiniz."
            ]
        elif 20 <= current_hour < 23:
            activities = [
                "Gece vakti yıldız gözlemlemek için fırsatlar sunar.",
                "Yerel gece hayatı veya müzik mekanlarının tadını çıkarabilirsiniz.",
                "Akşam gösterisi veya performansa katılabilirsiniz.",
                "Bir restoranda rahat bir akşam yemeği yiyebilirsiniz.",
                "Gece fotoğrafçılığı yürüyüşüne çıkabilirsiniz."
            ]
        else:
            activities = [
                "Geç gece, kitap okumak gibi rahatlatıcı aktiviteler için en iyisidir.",
                "Yatmadan önce film veya dizi izleyebilirsiniz.",
                "Rahatlama teknikleri veya meditasyon uygulayabilirsiniz.",
                "Yarınki aktivitelerinizi planlayabilirsiniz.",
                "Yarın için biraz dinlenebilirsiniz."
            ]
        
        # Rastgele bir aktivite seç
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

@views.route('/anasayfa', methods=['POST'])
@login_required
def get_weather():
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']

    API_KEY = get_api_key()
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={API_KEY}'# Aktivite �nerilerini olu�tur

    response = requests.get(url).json()
    city = response.get('name')
    temp = response.get('main', {}).get('temp')
    description = response.get('weather', [{}])[0].get('description')
    
    # Aktivite önerilerini oluştur
    recommender = ActivityRecommendation(temp, description)
    temp_activity = recommender.recommend_activity_based_on_temperature()
    weather_activity = recommender.recommend_activity_based_on_weather()
    time_activity = recommender.recommend_activity_based_on_time()

    # �u anki saati de g�nder
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
    
    # Yeni önerileri oluştur
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
    file_path = "api_key_txt"
    with open(file_path, 'r') as file:
        return file.read().strip()