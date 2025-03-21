document.addEventListener("DOMContentLoaded", function () {
    const status = document.querySelector('.status');
    const button = document.querySelector('.find-state');

    
    function findMyState() {
        status.textContent = 'Getting your location...';

        
        function success(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            status.textContent = 'Location found! Getting weather data...';

            
            fetch('/anasayfa', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ latitude: latitude, longitude: longitude })
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

                status.textContent = 'All information updated!';
            })
            .catch(error => {
                console.error("Error fetching weather data:", error);
                status.textContent = 'Error fetching weather data!';
            });
        }

        
        function error() {
            status.textContent = 'Unable to retrieve your location!';
        }

        
        navigator.geolocation.getCurrentPosition(success, error);
    }

    
    button.addEventListener('click', findMyState);
});