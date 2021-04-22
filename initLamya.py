import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import locale
import wikipedia
import translate
from translate import Translator
import pyjokes
from sound import Sound
import pyautogui
import time
import pyperclip  # handy cross-platform clipboard text handler
import screen_brightness_control as sbc
import socket
import sys
import webbrowser

chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))

lamiaIsHere=True
translator = Translator
listener = sr.Recognizer()
listener.energy_threshold = 400
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 
#engine.setProperty('rate', 1) 
test = False
r = sr.Recognizer()  
def talk(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        print("Je vous écoute ...")
        voice = listener.listen(source)
        r.pause_threshold =  1
    try:
        command = listener.recognize_google(voice,language="fr-FR")
        listener.phrase_threshold=2
        r.pause_threshold =  1
        print('vous avez dit : '+command)
        
        return command                         
    except:
        pass
def salutation():    
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        talk('Bonjour monsieur Skander!')

    if currentH >= 12 and currentH < 18:
        talk('Bonne après-midi monsieur Skander!')

    if currentH >= 18 and currentH !=0:
        talk('Bonsoir monsieur Skander!')
salutation()        
talk("comment puis-je vous aider ?")
while True:
    try:
        command2 = takeCommand()    
        if ('Bonjour'.upper() in command2.upper()) :
            talk("Bonjour monsieur skander")  
        elif ('facebook'.upper() in command2.upper()) :
            talk("D'accord !")
            webbrowser.open('https://www.facebook.com/')    
        elif ('gmail'.upper() in command2.upper()) :
            talk("D'accord !")
            webbrowser.open('https://mail.google.com/mail/u/0/')                          
        elif('je veux écouter'.upper() in command2.upper()):
            song = command2.upper().replace('je veux écouter','')
            talk("d'accord monsieur je vous mets "+song+" sur Youtube")
            pywhatkit.playonyt(song)
        elif('heure'.upper() in command2.upper()):
            talk('il est maintenant '+datetime.datetime.now().strftime('%H:%M'))
        elif('date'.upper() in command2.upper() or 'aujourd\'hui'.upper() in command2.upper()):
            locale.setlocale(category=locale.LC_ALL, locale='fr_FR.utf8')
            talk('aujourd\'hui on est le '+datetime.datetime.now().strftime('%A %d %B %Y'))
        elif('qui est '.upper() in command2.upper() or 'c\'est quoi '.upper() in command2.upper() or 'c\'est qui '.upper() in command2.upper() or 'comment est-ce qu\'on '.upper() in command2.upper() ):
            try:
                wikipedia.set_lang('fr')
                info=command2.upper().replace('qui est','')
                result=wikipedia.summary(info)
                talk('d\'apres wikipedia '+result)  
            except:
                talk('pardon mais je n\'ai pas trouvé de resultat')
        elif('blague'.upper() in command2.upper() ):
            blage=pyjokes.get_joke()
            traducteur = translate.Translator(to_lang="fr")
            translatedBlague = traducteur.translate(blage)
            print(translatedBlague)
            talk(translatedBlague)  
        elif('augmente le volume'.upper() in command2.upper() or 'augmente le son'.upper() in command2.upper()):
            for i in range(9):
                pyautogui.hotkey('volumeup')
                time.sleep(.01)
            talk('d\'accord monsieur, volume augmenté')       
        elif('coupe le volume'.upper() in command2.upper() or 'coupe le son'.upper() in command2.upper() ):
            talk('d\'accord monsieur, je coupe le volume')  
            pyautogui.hotkey('volumemute')
            time.sleep(.01)
        elif('baisse le volume'.upper() in command2.upper() or 'diminue le volume'.upper() in command2.upper() or  'diminue le son' in command2.upper() ):
            for i in range(9):
                pyautogui.hotkey('volumedown')
                time.sleep(.01)
            talk('d\'accord monsieur, volume baissé')   
        elif('volume à'.upper() in command2.upper() ):
            niveauVolume = command2.upper().replace('met le volume a','')
            print(niveauVolume)
            Sound.volume_set(niveauVolume)
            talk('d\'accord monsieur, volume baissé')  
        elif('qui es-tu'.upper() in command2.upper() ):
            talk('je suis lamya, j\'ai été programmé par monsieur skander ellouze')  
        elif('imprime écran'.upper() in command2.upper() ):
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'D:\py app\lamya\screenshots\ '+datetime.datetime.now().strftime('%A %d %B %Y %H %M %S')+'.jpg')
            talk('c\'est fait monsieur')  
        elif('lis la partie sélectionnée'.upper() in command2.upper() or 'lis'.upper() in command2.upper() ):
            def copy_clipboard():
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
                return pyperclip.paste()
            var = copy_clipboard()
            print(var)  
            talk('d\'accord monsieur '+var)        
        elif('copie la partie sélectionnée'.upper() in command2.upper() or 'copie'.upper() in command2.upper() or 'copier'.upper() in command2.upper() ):
            def copy_clipboard():
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
                return pyperclip.paste()
            var = copy_clipboard()
            print(var)  
            talk('c\'est fait monsieur.')     
        elif('colle'.upper() in command2.upper() or 'coller'.upper() in command2.upper()  ):
            def copy_clipboard():
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
                return pyperclip.paste()
            var = copy_clipboard()
            print(var)  
            talk('c\'est fait monsieur.') 
        elif('descends un peu'.upper() in command2.upper() or 'redescends un peu'.upper() in command2.upper()  ):
            pyautogui.hotkey('pagedown')
            time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
        elif('remonte un peu'.upper() in command2.upper() or 'monte un peu'.upper() in command2.upper()  ):
            pyautogui.hotkey('pagedown')
            time.sleep(.01) 
        elif('augmente la luminosité'.upper() in command2.upper()):
            sbc.set_brightness(sbc.get_brightness()+10)
            talk('d\'accord, la luminosité est a'+str(sbc.get_brightness()))
        elif('baisse la luminosité'.upper() in command2.upper() or 'diminue la luminosité'.upper() in command2.upper()):
            sbc.set_brightness(sbc.get_brightness()-10)
            talk('d\'accord, la luminosité est a'+ str(sbc.get_brightness()))
        elif('mets la luminosité à'.upper() in command2.upper() ):
            info=command2.upper().replace('mets la luminosité à ','')
            sbc.set_brightness(int(info))
            talk('d\'accord, la luminosité est a'+ str(sbc.get_brightness()))
        elif('adresse IP'.upper() in command2.upper() ):
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            talk('votre adresse ip est .'+ str(ip_address))              
        elif('instagram'.upper() in command2.upper()):
            webbrowser.get('chrome').open_new_tab("https://www.instagram.com/") 
            talk('d\'accord monsieur ')                     
        

        elif('lamia'.upper() in command2.upper()):
            talk('oui monsieur, je suis la')  
        elif('merci'.upper() in command2.upper()):
            talk('je vous emprie monsieur.')          
#        elif('tu peux partir' in command2.upper() ):
#            talk('d\'accord monsieur aurevoir.')  
#            lamiaIsHere=False
#            sys.exit()                    
        else:
            talk('je n\'ai pas bien compris est ce que vous pouvez repeté ?')  
        
        listener.stop()
    except:
        pass


#while lamiaIsHere: 
#    runLamya()       