import unittest
import time
from flask_testing import TestCase
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
        # Create a test user
        test_user = User(
            email='test@example.com',
            kullanıcı_adı='testuser',
            şifre='pbkdf2:sha256:260000$test_hashed_password'
        )
        db.session.add(test_user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class PageLoadingTimeTest(BaseTestCase):
    def test_home_page_loading_time(self):
        """Test if the homepage loads in less than 2 seconds"""
        start_time = time.time()
        response = self.client.get('/')
        end_time = time.time()

        load_time = end_time - start_time
        self.assertLess(load_time, 2.0, f"Page load time was {load_time} seconds, which exceeds the 2 second threshold")
        self.assert200(response)

    def test_login_page_loading_time(self):
        """Test if the login page loads in less than 2 seconds"""
        start_time = time.time()
        response = self.client.get('/giriş_yap')
        end_time = time.time()

        load_time = end_time - start_time
        self.assertLess(load_time, 2.0, f"Page load time was {load_time} seconds, which exceeds the 2 second threshold")
        self.assert200(response)

    def test_signup_page_loading_time(self):
        """Test if the signup page loads in less than 2 seconds"""
        start_time = time.time()
        response = self.client.get('/kayıt_ol')
        end_time = time.time()

        load_time = end_time - start_time
        self.assertLess(load_time, 2.0, f"Page load time was {load_time} seconds, which exceeds the 2 second threshold")
        self.assert200(response)

if __name__ == '__main__':
    unittest.main()