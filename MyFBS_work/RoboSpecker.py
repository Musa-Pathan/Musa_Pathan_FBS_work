import pyttsx3
text_speech = pyttsx3.init()

voices = text_speech.getProperty('voices')
text_speech.setProperty('voice', voices[1].id)  # Change index to select different voices
text_speech.setProperty('rate', 150)  # Adjust speech rate
text_speech.setProperty('pitch', 200)  # Adjust pitch
while True :
 text = input("enter text : ")
 if text == "q" :
   text_speech.say("thank you goood byy")
   break

 text_speech.say(text)
 text_speech.runAndWait()

