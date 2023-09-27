from tokenize import String
import requests
import json
import pyttsx3
engine = pyttsx3.init()
city=input("Enter the name of the city : \n")
url="http://api.weatherapi.com/v1/current.json?key=7e554481bab44b4a927192341232709&q="+city
r=requests.get(url)
# print(r.text)
msg=r.text
wdic=json.loads(r.text)
finalmsg=wdic["current"]["temp_c"]
engine.say("The current temperature in "+city+"is "+str(finalmsg))
engine.runAndWait()
# wdic=json.loads(r.text)
# print(wdic["location"])