from gtts import gTTS
import random
from playsound import playsound
import os
import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import datetime
import requests
import pyautogui
import pywhatkit
import time as tt
import subprocess
from PyMusic_Player import Music_Player_GUI


engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices) 
def speak(audio):
    engine.say(audio)
    engine.runAndWait() 
    
def getvoices(voice):
    voices = engine.getProperty('voices')
    #print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)


    if voice == 2:
        engine.setProperty('voice', voices[1].id)

sorucevap = ["iyiyim, siz nasılsınız efendim","süperim, siz nasılsınız efendim ","biraz keyifsizim, ya siz efendim","çok kötüyüm, siz nasılsınız efendim","kötüyüm, ya siz nasılsınız efendim"]
sorucevapcümleleri = ["nasılsın","naber","ne haber","napıyorsun","nasıl gidiyor","naber","napıyon","nasıl","nabıyon","ne yapıyorsun",]
kötüyümcevapları = ["Hayırdır efendim, neden kötüsünüz","Bunu duymak üzdü, umarım en yakın zamanda iyi olursunuz"]
iyiyimcevapları = ["Bunu duyduğuma sevindim efendim","Mutluluğunuz daim olsun efendim"]
kötüyümsözleri = ["Kötüyüm ya","Hiç iyi değilim","Kötüyüm","İyi değilim"]
iyiyimsözleri = ["İyiyim ya","Çok iyiyim","İyiyim"]

def record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        voice = r.listen(source)
        try:
            audio = r.recognize_google(voice, language="tr-TR")
        except sr.UnknownValueError:
            speak("Sizi Anlayamadım Efendim, tekrar söyler misiniz")
            return record()
        except sr.RequestError:
            speak("Sistemimde bir hata var efendim")
        except sr.WaitTimeoutError:
            speak("Üzgünüm sizi duyamadım, lütfen tekrar söyler misiniz")  
            return record()
        return audio             

def speak(string):
    tts = gTTS(string, lang="tr")    
    rand = random.randint(1,1000)
    file = 'ses+'+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
speak("Merhaba efendim, ben Mully, size nasıl yardımcı olabilirim efendim")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")# saat = I Dakika = M Saniye = S    
    speak("Anlık olarak zaman")
    speak(Time)  


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Anlık olarak tarih")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good morning sir!")
    elif hour >= 12 and hour <18: 
        speak("Good afternoon sir!")
    elif hour >= 18 and hour <24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")

def takeCommandCMD():
    query = input("Size nasıl yardımcı olabilirim\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="tr")  
        print(query)
    except Exception as e:

        print(e)
        return "None"
    return query    

def searchgoogle():
    speak("ne aramak istiyorsunuz")
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)


def screenshot():
    name_img = tt.time()
    name_img = f'C:\\Users\\kullanıcıadınız\\OneDrive\\Masaüstü\\Proje\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()


if __name__ == "__main__":
    getvoices(1)
    #wishme()
    while True:
        query = takeCommandMic().lower()
        if 'saat' in query:
            time()

        elif 'tarihteyiz' in query:
            date()       

        elif 'arama' in query:
            searchgoogle()

        elif 'youtube' in query:
            speak("youtube'da ne aramalıyım")
            topic = takeCommandMic()
            pywhatkit.playonyt(topic)
            speak("Youtube araması başarıyla yapıldı efendim")
            
        elif 'uyuyabilirsin' in query:
            speak("Uykuya dalıyorum efendim, görüşürüz.")
            quit() 

        elif 'ekran' in query:
            screenshot()    
        
        elif 'aç netflix' in query or 'netflix' in query or 'netflix aç' in query:
            wb.open("https://www.netflix.com/browse")
            speak("Netflix açılıyor efendim")


#arkadaşlar aynı şekilde sizlerde bu şekilde istediğiniz siteyi açtırabilirsiniz


        elif 'mailimi aç' in query or 'mailim' in query or 'aç mail' in query:
          wb.open("https://mail.google.com/mail/u/1/#inbox")
          speak("Mailiniz açılıyor efendim")

        elif 'instagramı aç' in query or 'aç instagram' in query or 'insta' in query:
            wb.open("https://www.instagram.com")
            speak("İnstagram açılıyor efendim.")
            pyautogui.sleep(2)

        elif 'müzik aç' in query or 'müzik başlat' in query or 'müziği ver' in query or 'ver müziği' in query or 'aç müziği' in query:
             songs_dir = 'C:\\Users\\onulb\\Music'# Müziklerinizin yüklü olduğu dosyanın konumunu yazmalısınız
             songs = os.listdir(songs_dir)
             os.startfile(os.path.join(songs_dir, songs[0]))
    

        elif "bilgisayarı kapat" in query or 'sistemi kapat' in query:
            os.system("shutdown /s /t 1")
            speak("Tamam, bilgisayarınız 10 saniye içerisinde kapanacak.")

        elif "bilgisayarı yeniden başlat" in query or 'sistemi yeniden başlat' in query:
            os.system("shutdown /r /t 1")
            speak("Tamam, bilgisayarınız 10 saniye içerisinde yeniden başlatılacak.")

        elif "oturumu kapat" in query or "sistemi kapat" in query:
            speak("Tamam, bilgisayarınızın 10 saniye içinde oturumu kapanacak.")
            subprocess.call(["shutdown", "/l"])
        
        elif query in sorucevapcümleleri:
            cevap = sorucevap 
            speak(random.choice(cevap))

        elif query in iyiyimsözleri:
            iyi = iyiyimcevapları
            speak(random.choice(iyi)) 

        elif query in kötüyümsözleri:
            kötü = kötüyümcevapları
            speak(random.choice(kötü))  