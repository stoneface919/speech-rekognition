import pyttsx3
import speech_recognition as sr
import yfinance as yf
import pyjokes
import webbrowser
import datetime 
import wikipedia as wp
import pywhatkit as pwk



# transform  voice to text - (listens to microphone and return audio as text)


def transform_text():
    r = sr.Recognizer()
    # configure microphone
    with sr.Microphone() as origin:
        r.pause_threshold(1)
        # informr that recording started
        print('You can talk now')
        # save input as text
        audio = r.listen(origin)
        
        try:
            # search in google what it listens
            search_query = r.recognize_google(audio, language='es-mx')
            # success test
            
            print(f'Your voice: {search_query}' )
        except sr.UnknownValueError:
            # test it did not recognize audio
            print('Upss, no idea what you are saying....')
            return 'Still waiting....'
        
        except sr.RequestError:
            
            print('Upss, service is available....')
            return 'Still waiting....'
            
        except:
            
            print('Upss, Something is wrong....')
            return 'Still waiting....'


transform_text()