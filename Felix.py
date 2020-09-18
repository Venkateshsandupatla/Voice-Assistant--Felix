import pyttsx3
import webbrowser
import speech_recognition as sr
import time
import os
from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen
import datetime
import wikipedia
import smtplib
engine = pyttsx3.init()
          

rate = engine.getProperty('rate')   
      
engine.setProperty('rate', 130)
            
print (rate)                   
print("welcome to ", end='')
pyttsx3.speak("hi this is  Felix  your perssonel assistant ")
                                                             
while True:
 r = sr.Recognizer()
 def newsRead():
    site = 'https://news.google.com/news/rss'
    op = urlopen(site)
    read = op.read()
    op.close()
    soup_page  = soup(read,'xml')   
    news_list = soup_page.findAll('item')
    for  news in news_list[:8]:
        print(news.title.text)
        pyttsx3.speak(news.title.text)  
      
        print(news.pubDate.text)
        print("--"*50)  
 def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourgmail.com', 'Password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
 def Greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        
       pyttsx3.speak("Hello Boss Good Morning")

    elif hour>=12 and hour<18:
           
        pyttsx3.speak("Hello Boss  Good Afternoon")   

    else:
          
        pyttsx3.speak("Hello Boss Good Evening")   
 with sr.Microphone() as s:
    pyttsx3.speak("how can i help you")
    r.adjust_for_ambient_noise(s)
    audio = r.record(s,duration=4) 
    print("speech done")
   
  
 ch =  r.recognize_google(audio,language="en-IN")
 
 print(ch)
  
 if "boring" in ch:

      pyttsx3.speak("opening some comedy clips to you")
      webbrowser.open("https://www.youtube.com/results?search_query=telugucomedyclips")
      time.sleep(5)
 elif "who" in ch and "you"  in ch and "are" in ch:
       pyttsx3.speak("Hello Boss   This is Felix version 1 point o your personnel assistant iam here to help you")
       
 elif ("created" in ch) or ("inventor" in ch) or ("creator" in ch): 
   pyttsx3.speak("My creator is venkatesh sandupatla  he is pursuing is btech in jawharlal nehru technological university and   student intern at linuxworld private limted here is his linkedin profile")
   webbrowser.open("https://www.linkedin.com/in/venkatesh-sandupatla-8a53a71aa")
   time.sleep(5)
 elif ("run" in ch) or ("open" in ch) and ("slack" in ch):
     pyttsx3.speak("opening slack")
     os.system("slack")
     time.sleep(4)
 elif "open" in ch or "run" in ch  and "gedit" in ch:
     os.system("gedit") 
     time.sleep(3) 
 
 elif ("date" in ch): 
       date = datetime.datetime.now()
       pyttsx3.speak(date)
       
 elif ("India" in ch):
      result = wikipedia.summary("India", sentences=2)
      pyttsx3.speak ("According to wikipedia")
      print(result)
      pyttsx3.speak(result)
      
      
 elif ("python" in ch):
       
      result = wikipedia.summary("Python", sentences=2)
      pyttsx3.speak ("According to wikipedia")
      print(result)
      pyttsx3.speak(result)
      
 elif ("laptop" in ch):
       r = wikipedia.search("laptop",results=4)
       print(r)
       
 elif "search" in ch and "YouTube" in ch:
       ch = ch.replace("search","")
       ch = ch.replace("in youtube","") 
       url =  "https://www.youtube.com/results?search_query="
       webbrowser.open(url+ch)
       time.sleep(7)
 elif "search" in ch and "Google":
       ch = ch.replace("search", "")
       ch = ch.replace("in google","")
       url = "http://www.google.com/search?q="
       webbrowser.open(url+ch)  
       time.sleep(5)
 elif "send email" in ch :
        try:
                pyttsx3.speak("What should i write in email?")
                content = input("What should i write?\n")
                pyttsx3.speak("Please Enter the recipient email!")
                to = input("Please Enter the recipient email!\n")    
                sendEmail(to, content)
                pyttsx3.speak("Email has been  successfully sent !")
        except Exception as e:
                print(e)
                pyttsx3.speak("Sorry boss !! . I am unable to send this email please try agian later")       
 elif "hai" in ch or "hello" in ch:
       Greetings()
 elif "exit" in ch:
        pyttsx3.speak("Im closing my services")
        pyttsx3.speak("Thank you sir")
        pyttsx3.speak("Have a nice day")
        exit()

      

          
 elif "news" in ch :
       newsRead()

 else:
     pyttsx3.speak("sorry i didnt get you")