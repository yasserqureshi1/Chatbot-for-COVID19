# ---------------------------------------------------------------------------
# Chatbot that asks health related questions to understand health of patient
# ---------------------------------------------------------------------------

# Used as a prototype in the CodeVsCOVID19 Hackathon
# Purpose is to reduce contact with victims of COVID19 virus as well as support hospitals by gathering patient data

import pyttsx3
import speech_recognition as sr
import textblob
import statistics
import time
import pandas as pd
import matplotlib.pyplot as plt

r = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()

questions = [
    'How are you feeling?',
    'How did you sleep?',
    # 'How tired do you feel?',
    # 'How does your cough feel',
    # 'Do you feel a loss of taste?',
    # 'Do you have difficulty breathing',
]

answers = []
sent_answers = []


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
                print("Listening...")
                audio = r.listen(source)

            print("Listening has stopped")

            try:
                ans = r.recognize_google(audio)
                print(ans)
            except:
                engine.say("Please say that again.")
                work = False

            if work == True:
                engine.say("You said:")
                engine.say(ans)
                engine.say("Is that correct?")
                engine.runAndWait()

                with mic as source:
                    print("Listening...")
                    check = r.listen(source)
                print("Listening has stopped")

                try:
                    checker = r.recognize_google(check)
                    print(checker)
                except:
                    checker = ''
                    work = False

                if "yes" in checker:
                    return ans
                else:
                    work = False


def sentiment(data):
    for i in range(len(data)):
        text = textblob.TextBlob(data[i])
        ans = text.sentiment.polarity
        sent_answers.append(int(ans))
    ave = statistics.mean(sent_answers)
    return ave


def plot():
    df = pd.read_csv('patientData.txt')
    plt.plot(df['Date'], df[' QnOne'])
    plt.title('Question One')
    plt.show()


def main():
    engine.say("Please answer the following questions using the scale 1 to 10, where 1 is bad and 10 is good.")
    answers.append(time.ctime())
    for i in range(len(questions)):
        b = AskQuestion(questions[i])
        ans = b.askquestion()
        answers.append(ans)

    with open('patientData.txt', 'a') as myfile:
        for i in range(len(answers)):
            myfile.write(answers[i])
            if i != (len(answers) - 1):
                myfile.write(', ')
        myfile.write('\n')

    #print('Average sentiment in answers is:', sentiment(answers))


if __name__ == '__main__':
    main()
    plot()
