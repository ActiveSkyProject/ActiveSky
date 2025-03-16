const findMyState = () => {
    const status = document.querySelector('.status');
  
    const success = (position) => {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
  
        status.textContent = `Latitude: ${latitude}, Longitude: ${longitude}`;
  
        // Flask backend'e gönderme
        fetch('/anasayfa', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ latitude: latitude, longitude: longitude })
        })
        .then(response => response.json())
        .then(data => {
            status.textContent = `Şehir: ${data.city}, Sıcaklık: ${data.temp}°C, Açıklama: ${data.description}`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    };
  
    const error = () => {
        status.textContent = 'Konum alınamadı!';
    };
  
    navigator.geolocation.getCurrentPosition(success, error);
  }
  
  document.querySelector('.find-state').addEventListener('click', findMyState);
  