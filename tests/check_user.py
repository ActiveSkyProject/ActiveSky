from website.models import User
from website import db
from website import create_app

# Flask uygulamasını başlat
app = create_app()

with app.app_context():
    user = User.query.filter_by(email="test@example.com").first()
    if user:
        print("Kullanıcı veritabanında var:", user.email)
    else:
        print("Kullanıcı veritabanında YOK!")
