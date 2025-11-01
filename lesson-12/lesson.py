# import random
# import example
# from calculator.calculate import add, subtract
# # import calculator.calculate as c


# # print(random.randint(1, 100))

# # print(type(random))

# # example.greeting()

# # print(type(example))

# print(add(1, 5))
# print(subtract(10, 5))
import speech_recognition as sr

recognizer = sr.Recognizer()

def speech_to_text():
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print('Recognizing...')

    text = recognizer.recognize_google(audio)
    
    print(f'You said {text}')

speech_to_text()