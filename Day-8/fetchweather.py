city=input("enter city>")
import requests
import time
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q={}".format(city)
url4 = "&appid=526152b2536498731308e71ea6af86bf"
'526152b2536498731308e71ea6af86bf'
url = url1 + url2 + url3+url4
jsondata = response.json()


tempreture=jsondata['main']['temp']
tempreture=tempreture-273.15
print("tempreture in {} is:{}".format(city,tempreture),"°C",sep="")


sunrise=jsondata['sys']['sunrise']
print("sunrise in {} at:{}".format(city,time.ctime(sunrise)))


sunset=jsondata['sys']['sunset']
print("sunset in {} at:{}".format(city,time.ctime(sunset)))


wind_speed=jsondata['wind']['speed']
print("wind speed in {} is:{}".format(city,wind_speed))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

