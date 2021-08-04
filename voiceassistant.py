from sys import exit
import speech_recognition as sr
from selenium import webdriver
from gtts import gTTS
import playsound
import time
import os
from time import ctime
import webbrowser
import smtplib
import bs4
import pyjokes
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import requests
import imdb
import winsound
import cv2
import pywhatkit as kit
from covid import Covid
def youtube(data):
    respond("what you want to play? ")
    query=listen()
    kit.playonyt(query)
def joke():
    respond(pyjokes.get_joke())
def coviddetail():
    covid = Covid(source="john_hopkins")
    #countries = covid.list_countries()
    #print(countries[:5])
    active = covid.get_total_active_cases()
    respond("total active cases in the world: {}".format(active))
    confirmed = covid.get_total_confirmed_cases()
    respond("total confirmed cases in the world: {}".format(confirmed))
    recovered = covid.get_total_recovered()
    respond("total cases in the world: {}".format(recovered))
    deaths = covid.get_total_deaths()
    respond("total deaths in the world: {}".format(deaths))
def news():
    news="http://news.google.com/news/rss"
    Client=urlopen(news)
    xml_page=Client.read()
    Client.close()
    soup_page=soup(xml_page,"xml")
    news_list=soup_page.findAll("item")
    for news in news_list:
        print(news.title.text)
        print(news.link.text)
        print(news.pubDate.text)
        print("_"*60)
def song():
    file="Alone.mp3"
    playsound.playsound(file)
def webcam():
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    respond("press escape to close webcam")
    while True:
        ret,frame=cap.read()
        frame=cv2.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
        cv2.imshow("input",frame)
        c=cv2.waitKey(1)
        if c==27:
            break
    cap.release()
    cv2.destroyAllWindows()
def timer():
    try:
        mytime=list(map(int,input("enter time in hr min sec\n").split()))
        if len(mytime)==3:
            total_seconds=mytime[0]*60*60+mytime[1]*60+mytime[2]
            time.sleep(total_seconds)
            frequency=3500
            duration=2000
            winsound.Beep(frequency,duration)
        else:
            respond("please enter time in correct format as mentioned\n")
            timer()
    except Exception as e:
        print("this is the exception ",e,"So!, please enter correct details")
        timer()
def movies():
    ia=imdb.IMDb()
    search=ia.get_top250_movies()
    for i in range(10):
        print(search[i])
        time.sleep(1)
def whatsapp():
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    respond('to whom you want to send the message')
    name = listen()
    respond('what message you want to send')
    msg = listen()
    input('Enter anything after scanning QR code')
    time.sleep(3)
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    time.sleep(5)
    user.click()
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    msg_box.send_keys(msg)
    button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
    button.click()
def weather():
    respond("At what place")
    city=listen()
    driver = webdriver.Chrome()
    driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")
    respond("here is the weather report of {}".format(city))
    respond(driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text)
def stopclock():
    respond("press enter to start the timer")
    while True:
        try:
            input()
            starttime=time.time()
            print("started")
            while True:
                print("time elasped:",round(time.time()-starttime,0),'secs',end='\n')
                time.sleep(1)
        except KeyboardInterrupt:
            print("stopped")
            endtime=time.time()
            print('totaltime:',round(endtime-starttime,2),'secs')
            break
def listen():
  r=sr.Recognizer()
  with sr.Microphone() as source:
    print("I am listening..")
    audio=r.listen(source,phrase_time_limit=10)
  data=""
  try:
    data=r.recognize_google(audio,language='en-US')
    print("you said: "+data)
  except sr.UnknownValueError:
    respond('Sorry i didnot get that')
    return listen()
  except sr.RequestError:
    respond("unable to fetch - Request Failed")
  return data
def respond(String):
    print(String)
    tts=gTTS(text=String,lang='en')
    tts.save("Speech.mp3")
    playsound.playsound("Speech.mp3")
    os.remove("Speech.mp3")
def voice_assistant(data):
    if "what is your name" in data:
        listening=True
        respond("My name is jarvis")
    elif "how are you" in data:
        listening=True
        respond("I am good {},thank you".format(name))
    elif "features" in data:
        listening=True
        respond("jokes\ncoronavirus details\nthe top news from google\nplay songs\nsend message in whatssapp\nsend mail\nsearching in google and wikipedia\nopening web cam\nwhether details of a place\ntimer\nthe top 10 movies according to imdb\nstopclock feature\nfinding location\ncurrent time\n")
    elif "current time" in data:
        listening=True
        respond(ctime())
    elif "joke" in data:
        listening=True
        joke()
    elif "youtube" in data.casefold():
        listening=True
        youtube(data)
    elif "news" in data:
        listening=True
        news()
    elif "timer" in data:
        listening=True
        timer()
    elif "movies" or "movie" in data:
        listening=True
        movies()
    elif "cam" in data:
        listening=True
        webcam()
    elif "stop clock" in data:
        listening=True
        stopclock()
    elif "open google" in data.casefold():
        listening=True
        respond("what you want to search")
        sear=listen()
        url='http://google.com/search?q='+sear
        respond("here is what I found for {}".format(sear))
        webbrowser.get().open(url)
    elif "find location" in data:
        listening=True
        respond("what is the location")
        location=listen()
        url='http://google.ml/maps/place/'+location+'/&amp;'
        respond("here is the location of {}".format(location))
        webbrowser.get().open(url)
    elif "weather" in data:
        listening=True
        weather()
    elif "mail" in data:
        listening=True
        respond("whom should I send email to?")
        to=listen()
        edict={'first person':'arunkumarreddy159@gmail.com','second person':'arunkumarreddy159@gmail.com','third person':'arunkumarreddy159@gmail.com'}
        toadd=edict[to]
        respond("what is the subject?")
        subject=listen()
        respond("what should i tell that person")
        message=listen()
        content='Subject: {}\n\n{}'.format(subject,message)
        mail=smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('qwertyforwork@gmail.com','jyppeoscgghmqlbf')
        mail.sendmail('qwertyforwork@gmail.com',toadd,content)
        mail.close()
        respond('Email Sent')
    elif "wiki" in data.casefold():
        listening=True
        respond("what should I search?")
        query=listen()
        response=requests.get("https://en.wikipedia.org/wiki/" +query)
        if response is not None:
            html=bs4.BeautifulSoup(response.text,'html.parser')
            paragraphs=html.select("p")
            intro=[i.text for i in paragraphs]
            halo=''.join(intro)
        respond(halo[:600])
    elif "whatsapp" in data.casefold():
        listening=True
        whatsapp()
    elif "song" in data:
        listening=True
        song()
    elif "coronavirus" in data:
        listening=True
        coviddetail()
    elif 'thank you' in data:
        listening=False
        print("Listening stopped")
        respond("See you {}".format(name))
    try:
        return listening
    except UnboundLocalError:
        print("time out")
if __name__ == "__main__": 
    respond("What's your name?") 
    name = listen() 
    respond("Hello, " + name + '.') 
    respond("{} password please..".format(name))
    password=listen()
    if password.casefold()!='hello':
        respond("sorry wrong password")
        exit()
    else:
        respond("access granted")
        time.sleep(1)
        respond("hello {},give me a command".format(name))
        listening=True
        while listening:
            data=listen()
            listening=voice_assistant(data)
