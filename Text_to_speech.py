import pyttsx3
import PySimpleGUI as sg

def speak(text, gender):
    
    engine = pyttsx3.init()

   
    voices = engine.getProperty('voices')
    if gender == 'male':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

   
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + 50)

    
    engine.say(text)
    engine.runAndWait()

sg.theme('DarkAmber')  

layout = [  [sg.Text('Enter Text to Speak:')],
            [sg.InputText(key='-IN-')],
            [sg.Text('Select Gender:')],
            [sg.Radio('Male', 'gender', key='-MALE-'), sg.Radio('Female', 'gender', key='-FEMALE-', default=True)],
            [sg.Text('Speaking Rate:')],
            [sg.Slider(range=(0, 200), orientation='h', size=(20, 15), default_value=100, key='-RATE-')],
            [sg.Button('Speak'), sg.Button('Cancel')] ]


window = sg.Window('Text to Speech', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  
        break
    if event == 'Speak': 
        text = values['-IN-']
        gender = 'male' if values['-MALE-'] else 'female'
        rate = values['-RATE-']
        speak(text, gender)
