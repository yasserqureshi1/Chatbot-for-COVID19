# Chatbot for COVID19

This chatbot was created as part of the CodeVsCOVID19 Hackathon 27/03/2020 to 30/03/2020.

*Website*: https://www.codevscovid19.org

The goal of this non-profit online hackathon is to develop a technical open-source prototype that provides a solution to address challenges regarding COVID-19 within 72 hours.

## Problem Identification: ##
We chose to address the problem of overcrowded and pressured hospitals as a result of the COVID19 pandemic.

## Our Solution: ##
Create a robot that can perform daily tasks that include:
- Sanitize infected areas using UV light
- Automated patient monitoring 
- Distribute hand sanitizer/masks

## Installation ##
Required modules for voice activated:
- pyttsx3
- speech_recognition
- textblob
- pandas
- matplotlib

Required moduled for hand detection:
- cv2
- numpy
- pyttsx3

## Details ##
In this repository is the Chatbot that will perfrom automated patient monitoring by asking specific symptom related questions. It would dictate questions and either take responses via voice or hand movement. Purpose of this is to reduce contact with the victims of the virus, so to not spread the virus.

The data collected can then be used to understand the patients symptoms throughout the stay at the hospital and thus understand when a patient is recovering. The chatbot includes a timeseries plot as well as sentiment analysis so to understand if the patient is generally feeling better or not.
