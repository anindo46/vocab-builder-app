import firebase_admin
from firebase_admin import credentials, db
import json
import streamlit as st

def init_firebase():
    if not firebase_admin._apps:
        firebase_key = json.loads(st.secrets["firebase_key"])
        cred = credentials.Certificate(firebase_key)
        firebase_admin.initialize_app(cred, {
            'databaseURL': st.secrets["databaseURL"]
        })
import firebase_admin
from firebase_admin import credentials, db
import json
import streamlit as st

def init_firebase():
    if not firebase_admin._apps:
        firebase_key = json.loads(st.secrets["firebase_key"])
        cred = credentials.Certificate(firebase_key)
        firebase_admin.initialize_app(cred, {
            'databaseURL': st.secrets["databaseURL"]
        })
