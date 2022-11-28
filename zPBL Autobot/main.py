import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source, timeout=2, phrase_time_limit=3)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command
    except:
        print('not working')
        pass
    return ''

def dishes(totalprice):
    talk(' which cuisine you would like to have')
    print('1.VEG\t2.NON-VEG\t3.CHINESE FOOD')
    command = take_command()
    print(command)



    if "two" in command or '2' in command or 'non veg' in command:
        talk('here find the menu')
        print('\t \t MENU')
        print('chicken chilli:120 \t  chicken tikka:250 \n \t\tchicken lolipop:150\t')
        command = take_command()
        if 'chicken chilli' in command:
            talk('your chicken chilli is comming')
            print('your chicken chilli is comming')
            totalprice += 120
            return totalprice
        if 'chicken tikka' in command:
            talk('your chiken tikka is comming')
            print('your chiken tikka is comming')
            totalprice += 250
            return totalprice
        if 'chicken lolipop' in command:
            talk('your chicken lolipop is comming')
            print('your chicken lolipop is comming')
            totalprice += 150
            return totalprice
        else:
            talk('sorry currently we cannot serve that item')
            talk('do you want to order anything else or go back to main menu')
            talk('say manu to go to main menu or dishes to order')
            command = take_command()
            if 'menu' in command:
                return totalprice
            if 'dishes' in command:
                totalprice = dishes(totalprice)
                return totalprice
    elif "one" in command or '1' in command or 'veg' in command:
        talk('here find the menu')
        print('\t \t MENU')
        print('  Idly:30 \t  Vada Sambhar:25 \n \t\tPav Bhaji:60\t')
        command = take_command()
        if 'idly' in command or 'idli' in command:
            talk('your idly is comming')
            print('your idly is comming')
            totalprice += 30
            return totalprice
        elif 'Vada Sambhar' in command:
            talk('your Vada Sambhar is comming')
            print('your Vada Sambhar is comming')
            totalprice += 25
            return totalprice
        elif 'Pav Bhaji' in command or 'Pav Bhajy' in command:
            talk('your Pav Bhaji is comming')
            print('your Pav Bhaji is comming')
            totalprice += 60
            return totalprice
        else:
            talk('sorry currently we cannot serve that item')
            talk('do you want to order anything else or go back to main menu')
            talk('say manu to go to main menu or dishes to order')
            command = take_command()
            if 'menu' in command:
                return totalprice
            if 'dishes' in command:
                totalprice = dishes(totalprice)
                return totalprice

    elif "three" in command or '3' in command or 'chinese food' in command:
        talk('here find the menu')
        print('\t \t MENU')
        print('noodels:50 \t  momos:80 \n \t\tfired rice:50\t')
        command = take_command()
        if 'noodels' in command:
            talk('your noodels is comming')
            print('your noodels is comming')
            totalprice += 50
            return totalprice
        if 'momos' in command:
            talk('your momos is comming')
            print('your momos is comming')
            totalprice += 80
            return totalprice
        if 'fired rice' in command:
            talk('your fired rice is comming')
            print('your fired rice is comming')
            totalprice += 50
            return totalprice
        else:
            talk('sorry currently we cannot serve that item')
            talk('do you want to order anything else or go back to main menu')
            talk('say manu to go to main menu or dishes to order')
            command = take_command()
            if 'menu' in command:
                return totalprice
            if 'dishes' in command:
                totalprice = dishes(totalprice)
                return totalprice

    return totalprice

def run_alexa():
    global totalprice
    print('try with hi , how are you ,')
    command = take_command()
    print('running bot ', command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)


    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'how are you' in command:
        talk('I am fine. How you are doing')
        print('I am fine.\n How you are doing')
    elif 'i am fine ' in command or 'i am doing great' in command or 'i am good ' in command or 'fine' in command or 'we are fine' in command:
        talk('sounds good. How can I help you')
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'you like alexa' in command:
        talk('ya! i have a crush on her')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'hi' in command or 'hai' in command:
        talk('hello ise 4 a section im your friendly chat bot and im here for your assistance')
        talk(' how are you doing ')
    elif 'terminate' in command or 'bye' in command or 'we are leaving' in command:
        talk('your bill is ' + str(totalprice))
        print(totalprice)
        talk('we would be happy to see you again')
        exit(0)
    elif 'menu' in command or 'venue' in command or 'manu' in command or 'new' in command or 'feeling hungry' in command:
        totalprice = dishes(totalprice)
    else:
        talk('Please say the command again.')
        talk('or try with something else')
totalprice = 0

while True:
    run_alexa()
