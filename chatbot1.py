import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()


class AskQuestion:
    def __init__(self, quest):
        self.__quest = quest
        self.__answer = None
        self.__understood = None

    def askquestion(self):
        while True:
            work = True
            engine.say(self.__quest)
            engine.runAndWait()

            with mic as source:
                print("listening...")
                audio = r.listen(source)

            print("Listening has stopped")

            try:
                a = r.recognize_google(audio)
                print(a)

            except:
                engine.say("Please say that again.")
                work = False

            if work == True:
                return a


def start():
    questions = [
        'How are you feeling?',
        'How did you sleep?',
        'Do you feel tired?',
        'Have you been coughing',
        'Do you feel a loss of taste?',
        'Do you have difficulty breathing',
    ]


    for i in range(len(questions)):
        b = AskQuestion(questions[i])
        ans = b.askquestion()

start()