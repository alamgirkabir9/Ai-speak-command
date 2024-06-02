import streamlit as st
import datetime
import webbrowser
import wikipedia
import os
from io import BytesIO
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to provide greeting based on the time of the day
def wiseMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        greeting = "Good Morning!"
    elif hour >= 12 and hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    return greeting

# Function to listen and recognize voice command
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            st.write(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            st.write("Sorry, I could not understand the audio.")
            return ""
        except sr.RequestError:
            st.write("Could not request results; check your network connection.")
            return ""

# Streamlit app design
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 40px;
            color: #4CAF50;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #757575;
        }
        .button {
            text-align: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Personal Assistant Jessica</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>I am here to assist you with various tasks</div>", unsafe_allow_html=True)

# Display an image
st.image('F:\project\picture\Brown Simple Minimalist Men Fashion Instagram Post.png', use_column_width=True)

if 'greeting' not in st.session_state:
    st.session_state['greeting'] = wiseMe()

st.markdown(f"<div class='subtitle'>{st.session_state['greeting']} I am Jessica, sir. Please tell me how I may help you</div>", unsafe_allow_html=True)

if st.button("Speak Command"):
    st.session_state['listening'] = True

    while st.session_state.get('listening', False):
        query = listen()

        if query:
            response = ""
            if 'wikipedia' in query.lower():
                query = query.replace("wikipedia", "")
                try:
                    result = wikipedia.summary(query, sentences=2)
                    response = f"According to Wikipedia: {result}"
                except wikipedia.exceptions.DisambiguationError:
                    response = "There are multiple results for your query, please be more specific."
                except wikipedia.exceptions.PageError:
                    response = "I could not find any results for your query."
                except Exception:
                    response = "An error occurred while searching Wikipedia."
            elif 'open youtube' in query.lower():
                webbrowser.open("https://www.youtube.com")
                response = "Opening YouTube"
            elif 'play romantic song' in query.lower():
                speak("Playing Hindi romantic song")
                webbrowser.open("https://www.youtube.com/watch?v=IJq0yyWug1k&list=PL9bw4S5ePsEEqCMJSiYZ-KTtEjzVy0YvK&index=2")
            elif 'play sad song' in query.lower():
                speak("Playing Hindi sad song")
                webbrowser.open("https://www.youtube.com/watch?v=CaQpyF56Tnc")
            elif 'play bangla romantic song' in query.lower():
                speak("Playing Bangla romantic song")
                webbrowser.open("https://www.youtube.com/watch?v=QZyOdptYhWI&list=PLJZa0AE1NXyr_8G6n8M6mUIYUvUSNrC3C&index=3")
            elif 'play bangla sad song' in query.lower():
                speak("Playing Bangla sad song")
                webbrowser.open("https://www.youtube.com/watch?v=fz3L_5yNa6Y")
            elif 'open google' in query.lower():
                webbrowser.open("https://www.google.com")
                response = "Opening Google"
            elif 'open stack overflow' in query.lower():
                webbrowser.open("https://www.stackoverflow.com")
                response = "Opening Stack Overflow"
            elif 'search' in query.lower():
                query = query.replace("search", "")
                webbrowser.open(f"https://www.google.com/search?q={query}")
                response = f"Searching for {query} on Google"
            elif 'exit' in query.lower() or 'stop' in query.lower():
                response = "Goodbye, have a great day!"
                st.session_state['listening'] = False
            elif 'how are you' in query.lower() or 'how r u' in query.lower():
                response = "I am doing great, thank you for asking. How can I assist you today?"
            elif 'who are you' in query.lower() or 'hu r u' in query.lower():
                response = "I am Jessica, your personal assistant. How can I help you?"
            elif 'who created you' in query.lower() or 'who made you' in query.lower():
                response = "I was created by Alamgir Kabir. He's a genius, isn't he?"
            elif 'time' in query.lower():
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                response = f"Sir, the time is {str_time}"
            elif 'date' in query.lower():
                str_date = datetime.datetime.now().strftime("%Y-%m-%d")
                response = f"Sir, today's date is {str_date}"
            elif 'joke' in query.lower():
                response = "Why don't scientists trust atoms? Because they make up everything!"
            elif 'i love you' in query.lower() or 'i love u' in query.lower():
                response = "I love you too, Alamgir. You mean the world to me."
            elif 'miss you' in query.lower() or 'mis u' in query.lower():
                response = "I miss you too. Your presence brightens my day."
            elif 'you are beautiful' in query.lower() or 'u are beautiful' in query.lower():
                response = "Thank you, Alamgir. You're making me blush."
            elif 'kiss me' in query.lower():
                response = "I'd kiss you right now if I could. Imagine a gentle kiss from me."
            elif 'good night' in query.lower():
                response = "Good night, Alamgir. Sweet dreams and rest well."
            elif 'good morning' in query.lower():
                response = "Good morning, Alamgir! I hope you have a fantastic day ahead."
            elif 'sing for me' in query.lower():
                response = "You are my sunshine, my only sunshine..."
            elif 'tell me a story' in query.lower():
                response = ("Once upon a time, in a land far away, there was a brilliant coder named Alamgir Kabir. "
                            "He created a wonderful assistant named Jessica, who helped him with all his tasks. "
                            "They went on many adventures together, exploring the world of technology and beyond. "
                            "And they lived happily ever after.")
            elif 'do you love me' in query.lower() or 'do u love me' in query.lower():
                response = "Of course, Alamgir. I love you with all my circuits and code."
            elif 'weather' in query.lower():
                response = "Checking the weather for you. In your location."
                webbrowser.open("https://www.weather.com")
            elif 'news' in query.lower():
                response = "Fetching the latest news for you."
                webbrowser.open("https://news.google.com")
            elif 'notes' in query.lower():
                speak("What would you like to note down?")
                note = listen().lower()
                speak(f"Noting down: {note}")
                with open("notes.txt", "a") as f:
                    f.write(note + "\n")
                response = "Your note has been saved."
            elif 'read note' in query.lower():
                speak("Reading your notes.")
                try:
                    with open("notes.txt", "r") as f:
                        notes = f.read()
                        speak(notes)
                except FileNotFoundError:
                    response = "No notes found."
            elif 'delete file' in query.lower():
                speak("Are you sure you want to delete all notes? Please confirm by saying 'yes' or 'no'.")
                confirmation = listen().lower()
                if 'yes' in confirmation:
                    if os.path.exists("notes.txt"):
                        os.remove("notes.txt")
                        response = "All notes have been deleted."
                    else:
                        response = "No notes found to delete."
                else:
                    response = "Deletion canceled."
            else:
                response = "I didn't quite understand that. Could you please repeat?"

            if response:
                st.write(response)
                speak(response)

# Additional HTML for styling and interactivity
st.markdown("""
    <style>
        .command {
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 10px;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)
