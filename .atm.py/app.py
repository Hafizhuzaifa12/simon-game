import streamlit as st
import speech_recognition as sr
import tempfile
import os

st.title("Speech Recognition App")

recognizer = sr.Recognizer()

# Upload audio file
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "opipgg"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
        temp_audio.write(uploaded_file.read())
        temp_audio_path = temp_audio.name
    
    # Recognizing speech
    with sr.AudioFile(temp_audio_path) as source:
        st.info("Processing audio...")
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            st.success("Transcription:")
            st.write(text)
        except sr.UnknownValueError:
            st.error("Could not understand the audio.")
        except sr.RequestError:
            st.error("Could not request results from Google Speech Recognition service.")
    
    os.remove(temp_audio_path)