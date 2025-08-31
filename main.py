import speech_recognition as sr
import pyaudio as pa
import webbrowser
import pyttsx3
import music
import news
import google.generativeai as genai
import re
import asyncio
import pyautogui
import uuid
from Reminder import reminder

recognizer = sr.Recognizer()


# Speak Function
def speak(text):
    # print(f"[Speaking]: {text}")
    engine = pyttsx3.init(driverName="sapi5")   
    engine.say(text)
    engine.runAndWait()



# Process Command
def processCommand(c):
    print("Alexa activated....")
    if "open google" in c.lower():
        webbrowser.open_new_tab("https://www.google.com/")
    elif "open youtube" in c.lower():
        webbrowser.open_new_tab("https://www.youtube.com/")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music.music_collection[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        joke = news.final_ans
        speak(joke)

    elif "remind" in c.lower():
        print("reminder on")

        if "remind" in c.lower():
            task = c.lower().split("that")[1]
        try:
            match = re.search(r'\d+', c)
            if match:
                time = int(match.group())
        except Exception as e:
            pass

        async def main():
            await reminder("study", time)
            speak(f"do you {task}" )
        asyncio.run(main())


    elif "screenshot" in c.lower():
        print("Screenshort function is called")
        screenshort = pyautogui.screenshot()
        id = uuid.uuid1()
        screenshort.save(f"Images/{id}.jpg")
        speak("screenshot taken succesfuly")
    
    else:
        genai.configure(api_key="AIzaSyAaHJE2yTt9DxHQ2qyxhQG1sfrq86gF4To")

        # Initialize the model you want to use. 'gemini-pro' is a good choice for text-only prompts.
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Send a prompt to the model and get a response.
        response = model.generate_content(c)
        data=response.text
        speak(data)


if __name__== "__main__":
    speak("Nexora initializing...")
    while True:
        # listening wake up call for Alexa!
        try:
            with sr.Microphone() as source:
                # Capture audio
                # recognizer.adjust_for_ambient_noise(source, duration=1)  # optional
                print("Listening.....")
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=1)
                # Convert speech to text
                text = recognizer.recognize_google(audio)
                print("You said:", text)



                if "nexora" in text.lower():
                    speak("Yaa")
                    with sr.Microphone() as source:
                        print("Alexa Activated Listening....")
                        # Capture audio
                        # recognizer.adjust_for_ambient_noise(source, duration=1)  # optional
                        audio = recognizer.listen(source, timeout=4, phrase_time_limit=10)
                        # Convert speech to text
                        text = recognizer.recognize_google(audio)
                        print(text)
                        processCommand(text)

        except Exception as e:
            print("Error; {0}".format(e))
            