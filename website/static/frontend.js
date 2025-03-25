document.addEventListener("DOMContentLoaded", function () {
    const status = document.querySelector('.status');
    const findButton = document.querySelector('.find-state');
    const changeButton = document.querySelector('.change');

    let weatherData = null;

    function findMyState() {
        status.textContent = 'Konum alınıyor...';

        function success(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            status.textContent = 'Konum bulundu! Hava durumu alınıyor...';

            fetch('/anasayfa', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ latitude, longitude })
            })
                .then(response => response.json())
                .then(data => {
                    document.getElementById("city-name").innerText = data.city;
                    document.getElementById("temperature").innerText = data.temp;
                    document.getElementById("weather-description").innerText = data.description;
                    document.getElementById("current-time").innerText = data.current_time;

                    document.getElementById("temp-activity").innerText = data.temp_activity;
                    document.getElementById("weather-activity").innerText = data.weather_activity;
                    document.getElementById("time-activity").innerText = data.time_activity;

                    weatherData = data;
                    status.textContent = 'Bilgiler güncellendi!';
                })
                .catch(error => {
                    console.error("Hata:", error);
                    status.textContent = 'Hava durumu verisi alınırken hata oluştu!';
                });
        }

        function error() {
            status.textContent = 'Konum alınamadı!';
        }

        navigator.geolocation.getCurrentPosition(success, error);
    }

    function changeActivities() {
        if (!weatherData) {
            alert("Önce hava durumunu alınız!");
            return;
        }

        fetch("/change_activities", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                temp: weatherData.temp,
                description: weatherData.description
            })
        })
            .then(response => response.json())
            .then(data => {
                document.getElementById("temp-activity").innerText = data.temp_activity;
                document.getElementById("weather-activity").innerText = data.weather_activity;
                document.getElementById("time-activity").innerText = data.time_activity;
            })
            .catch(error => {
                console.error("Hata:", error);
                alert("Önerileri güncellerken hata oluştu!");
            });
    }

    findButton.addEventListener('click', findMyState);
    changeButton.addEventListener('click', changeActivities);
});