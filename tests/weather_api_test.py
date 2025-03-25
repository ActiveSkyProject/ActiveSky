import unittest
from flask_testing import TestCase
from werkzeug.security import generate_password_hash
from website import create_app, db
from website.models import User

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:database.db'
    SECRET_KEY = "f9287f9345097c64f11a54d810f001eb"
    WTF_CSRF_ENABLED = False

class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app()
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class WeatherAPITest(BaseTestCase):
    def test_weather_api_response(self):
        """Test if the weather API endpoint returns valid data"""
        with self.client:
            # Use generate_password_hash for user creation
            test_user = User(
                email='api_test@example.com',
                kullanıcı_adı='apiuser',
                şifre=generate_password_hash('apipassword')
            )
            db.session.add(test_user)
            db.session.commit()

            # Login with the test user
            login_response = self.client.post('/giriş_yap', data={
                'email': 'api_test@example.com',
                'şifre': 'apipassword'
            }, follow_redirects=True)

            # Check login success HTTP kodu 200 degilse fail
            self.assert200(login_response, "Login failed for API test")

            # API test coordinates (enlem boylam)
            test_coords = {'latitude': 41.0082, 'longitude': 28.9784}

            # Weather API call post istegi gonderiliyor
            response = self.client.post('/anasayfa', json=test_coords, content_type='application/json')

            # Check API response
            self.assert200(response, "API call failed. Expected 200, got different status")

            data = response.json

            # Check for expected fields her alana bakılır bos olan varsa hata doner
            required_fields = ['city', 'temp', 'description', 'current_time', 'temp_activity', 'weather_activity', 'time_activity']

            for field in required_fields:
                self.assertIn(field, data, f"Expected field missing: {field}")
                self.assertIsNotNone(data[field], f"Field returned empty: {field}")

if __name__ == '__main__':
    unittest.main()