import firebase_admin
from firebase_admin import credentials, db

def init_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("firebase_key.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://YOUR_PROJECT_ID.firebaseio.com/'  # 🔁 Replace with your actual DB URL
        })
