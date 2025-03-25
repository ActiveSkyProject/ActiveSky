import unittest
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

class UserRegistrationTest(BaseTestCase):
    def test_user_registration_success(self):
        """Test if a new user can register successfully"""
        response = self.client.post('/kayıt_ol', data={
            'email': 'new@example.com',
            'kullanıcı_adı': 'newuser',
            'şifre': 'password123'
        }, follow_redirects=True)

        self.assert200(response)
        # Check for success message in response
        self.assertIn(b'Hesap ba\xc5\x9far\xc4\xb1yla olu\xc5\x9fturuldu.', response.data)

        # Verify user exists in database
        user = User.query.filter_by(email='new@example.com').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.kullanıcı_adı, 'newuser')

    def test_user_registration_existing_email(self):
        """Test if registration fails with existing email"""
        response = self.client.post('/kayıt_ol', data={
            'email': 'test@example.com',  # Already exists from setUp
            'kullanıcı_adı': 'anotheruser',
            'şifre': 'password123'
        }, follow_redirects=True)

        self.assert200(response)
        # Check for error message in response
        self.assertIn(b'Bu email sistemde bulunmaktad\xc4\xb1r.', response.data)

    def test_user_registration_short_email(self):
        """Test if registration fails with short email"""
        response = self.client.post('/kayıt_ol', data={
            'email': 'a@b',
            'kullanıcı_adı': 'shortuser',
            'şifre': 'password123'
        }, follow_redirects=True)

        self.assert200(response)
        # Check for error message in response
        self.assertIn(b'Email en az 4 karakter olmal\xc4\xb1d\xc4\xb1r.', response.data)

    def test_user_registration_short_username(self):
        """Test if registration fails with short username"""
        response = self.client.post('/kayıt_ol', data={
            'email': 'valid@example.com',
            'kullanıcı_adı': 'a',
            'şifre': 'password123'
        }, follow_redirects=True)

        self.assert200(response)
        # Check for error message in response
        self.assertIn(b'Kullan\xc4\xb1c\xc4\xb1 ad\xc4\xb1 en az 2 karakter olmal\xc4\xb1d\xc4\xb1r.', response.data)

    def test_user_registration_short_password(self):
        """Test if registration fails with short password"""
        response = self.client.post('/kayıt_ol', data={
            'email': 'valid@example.com',
            'kullanıcı_adı': 'validuser',
            'şifre': 'short'
        }, follow_redirects=True)

        self.assert200(response)
        # Check for error message in response
        self.assertIn(b'\xc5\x9eifre en az 7 karakter olmal\xc4\xb1d\xc4\xb1r.', response.data)

if __name__ == '__main__':
    unittest.main()