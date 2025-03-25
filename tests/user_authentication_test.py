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

class UserAuthenticationTest(BaseTestCase):
    def test_user_login_success(self):
        """Test if a user can log in with correct credentials"""
        # Create a user with properly hashed password
        plain_password = 'password123'
        hashed_password = generate_password_hash(plain_password)
        
        new_user = User(
            email='new@example.com',
            kullanıcı_adı='newuser',
            şifre=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        
        # Login test with proper password
        response = self.client.post('/giriş_yap', data={
            'email': 'new@example.com',
            'şifre': plain_password
        }, follow_redirects=True)

        self.assert200(response)
        # Decode response data to handle Turkish characters correctly
        response_text = response.data.decode('utf-8')
        self.assertIn('Başarıyla giriş yapıldı', response_text)

    def test_user_login_wrong_password(self):
        """Test if login fails with incorrect password"""
        response = self.client.post('/giriş_yap', data={
            'email': 'test@example.com',
            'şifre': 'wrong_password'
        }, follow_redirects=True)

        self.assert200(response)
        response_text = response.data.decode('utf-8')
        self.assertIn('Hatalı şifre girildi', response_text)

    def test_user_login_nonexistent_email(self):
        """Test if login fails with non-existent email"""
        response = self.client.post('/giriş_yap', data={
            'email': 'nonexistent@example.com',
            'şifre': 'any_password'
        }, follow_redirects=True)

        self.assert200(response)
        response_text = response.data.decode('utf-8')
        self.assertIn('Bu email sistemde bulunmamaktadır', response_text)

if __name__== '__main__':
    unittest.main()