#test_config.py
class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use in-memory database for tests
    SECRET_KEY = "f9287f9345097c64f11a54d810f001eb"
    WTF_CSRF_ENABLED = False  # Disable CSRF protection for testing