import streamlit as st
import requests
import json
import datetime
from firebase_init import init_firebase
from firebase_admin import db

# Initialize Firebase
init_firebase()

# Streamlit App UI
st.set_page_config(page_title="📘 IELTS Vocabulary Builder", layout="centered")
st.title("📘 Multi-User IELTS Vocabulary Builder")

# Login
username = st.text_input("👤 Enter your name (for tracking)").strip().lower()

# Word Input
word = st.text_input("✍️ Enter an English word").strip().lower()

# Function to fetch word data from Dictionary API
def get_word_data(word):
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        res = requests.get(url)
        data = res.json()[0]
        meaning = data['meanings'][0]['definitions'][0]['definition']
        synonyms = data['meanings'][0].get('synonyms', [])
        example = data['meanings'][0]['definitions'][0].get('example', '')
        return meaning, synonyms, example
    except:
        return "Meaning not found", [], ""

# Submit button
if st.button("➕ Add Word") and username and word:
    meaning, synonyms, example = get_word_data(word)
    word_data = {
        'word': word,
        'meaning': meaning,
        'synonyms': synonyms,
        'example': example,
        'added_by': username,
        'timestamp': datetime.datetime.now().isoformat()
    }

    ref = db.reference(f"vocab")
    ref.child(word).set(word_data)
    st.success(f"✅ Word '{word}' added by {username}!")

# Display all words
st.subheader("📚 All Shared Vocabulary (A–Z Sorted)")
ref = db.reference("vocab")
words_dict = ref.get()

if words_dict:
    sorted_words = sorted(words_dict.items(), key=lambda x: x[0])
    for word, data in sorted_words:
        st.markdown(f"### 🔤 {word.title()}")
        st.write(f"**Meaning:** {data['meaning']}")
        st.write(f"**Synonyms:** {', '.join(data['synonyms']) if data['synonyms'] else 'None'}")
        st.write(f"**Example Sentence:** _{data['example']}_")
        st.caption(f"👤 Added by: `{data['added_by']}` on {data['timestamp'][:10]}")
else:
    st.info("No words added yet. Start by entering one above.")
