import json
from difflib import get_close_matches
import pyttsx3


engine=pyttsx3.init()
new_voice_rate=115
engine.setProperty('rate', new_voice_rate)


def speak(text):
    if type(text) == list:
        l=len(text)
        i=0
        while(i < l):
            if(i == l-1):

                engine.say(str(text[i]))
                engine.runAndWait()
                i=i+1
            else:
                engine.say(str(text[i]))
                engine.say('it has another defination too ')
                engine.runAndWait()
                i=i+1
    else:
        engine.say(str(text))

    



word_file=json.load(open('data.json'))
def find_meaning():
    word=input('Please input any word : ')
    word=word.lower()
    if word in word_file:
        print("\n".join(word_file[word]))
        speak(word_file[word])
    elif len(get_close_matches(word, word_file.keys())) > 0:
        print(f'Did you mean %s instead of {word}? press Y if so else press N :' % get_close_matches(word, word_file.keys())[0])
        engine.say(f'Did you mean {get_close_matches(word, word_file.keys())[0]} instead of {word}? press Y if so else press N :' )
        engine.runAndWait()
        y=input('Type Y or N : ')
        if y == 'Y':
            speak(word_file[get_close_matches(word, word_file.keys())[0]])
        elif y == 'N':
            print('We didnot able to find what you are looking ')
            engine.say('We didnot able to find what you are looking ')
            engine.runAndWait()
        else:
            print('we dont understand your entry')
            engine.say('we dont understand your entry')
            engine.runAndWait()
    else:
        print('The word does not exist')
        engine.say('The word does not exist')
        engine.runAndWait()

find_meaning()
