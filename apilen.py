#import requests
#import html2text
#s=requests.get('https://golos.io')
#d=html2text.HTML2Text().handle(s.text)
#print(d)
#import requests
#import json
#s=requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=BTC-GBG')
#data= s.json()
#k = data['result'][0]['Last']
#print("%.8f" % k)
#import requests, bs4
#s=requests.get("https://sinoptik.com.ru/погода-москва")
#b=bs4.BeautifulSoup(s.text, "html.parser")
#p3=b.select('.temperature .p3')
#pogoda1=p3[0].getText()
#p4=b.select('.temperature .p4')
#pogoda2=p4[0].getText()
#p5=b.select('.temperature .p5')
#pogoda3=p5[0].getText()
#p6=b.select('.temperature .p6')
#pogoda4=p6[0].getText()
#print("Утром--" + pogoda1 + '' + pogoda2)
#print("Днем--" + pogoda3 + '' + pogoda4)
#p=b.select('.rSide .description')
#pogoda=p[0].getText()
#print(pogoda.strip())
#import requests
#url="http://wsf.cdyne.com/WeatherWS/Weather.asmx?WSDL"
#headers = {'content-type': 'application/soap+xml'}
#headers = {'content-type': 'text/xml'}
#body = """<?xml version="1.0" encoding="UTF-8"?>
#         <SOAP-ENV:Envelope xmlns:ns0="http://ws.cdyne.com/WeatherWS/" xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/" 
#            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
#            <SOAP-ENV:Header/>
#              <ns1:Body><ns0:GetWeatherInformation/></ns1:Body>
#         </SOAP-ENV:Envelope>"""

#response = requests.post(url,data=body,headers=headers)
#print(response.content)



#import requests
#url=""

#import random 
#import string
#x = str(input("Введите первую букву или цифру: "))
#y = str(input("Введите вторую букву или цифру: "))
#if x.isdigit() and y.isdigit():
#    x = int(x)
#    y = int(y)
#    if x>y:
#        print("Случайное число: ",random.randint(y,x))  
#    else:
#        print("Случайное число: ",random.randint(x,y))
#elif x.isdigit() or y.isdigit() != False:
#    print("Вы ввели цифру и букву одновременно")                
#else:
#    x = x.lower()
#    y = y.lower()
#    ctroka = string.ascii_lowercase
#    zx = ctroka.index(x)
#    zy = ctroka.index(y) 
#    if zx > zy:
#        srez = random.choice(ctroka[zy:zx])
#        print("Случайная буква:",srez)
#    else:
#        srez = random.choice(ctroka[zx:zy])
#        print("Случайная буква:",srez)     
#x = input('Insert first letter:')
#y = input('Insert second letter:')
#c=

#import random 
#import string
#x = input("Insert First character:")
#y = input("Insert Second Character:")
#z = string.ascii_lowercase
#x = x.lower()
#y = y.lower()
#x1= z.index(x)
#y1= z.index(y)
#if x1 > y1:
#    rast=x1-y1
#    print("Индекс первой буквы - {}, второй - {}, расстояние между ними {}".format(x1,y1,rast))

#import string
#x = input("Ввведите первую букву:")
#y = input("Введите вторую букву:")
#z = string.ascii_lowercase
#x = x.lower()
#y = y.lower()
#x1= z.index(x)
#y1= z.index(y)
#if x1 > y1:
#    rast=x1-y1
#    print("Индекс первой буквы - {}, второй - {}, расстояние между ними {}".format(x1,y1,rast))
#else:
#    rast=y1-x1
#    print("Индекс первой буквы - {}, второй - {}, расстояние между ними {}".format(x1,y1,rast))
#print(z.index(x))


#import string
#x = int(input("Введите номер буквы:"))
#alf = string.ascii_lowercase
#letter= alf[x]
#print(letter)

#a = int(input("Insert first integer:"))
#b = int(input("Insert second integer:"))
#c = int(input("Insert Third integer"))

#if b < a < c or c < a < b:
#    print('Среднее:', a)
#elif a < b < c or c < b < a:
#    print('Среднее:', b)
#else:
#    print('Среднее:', c)




year=input('Введите год для проверки:')
if year.isdigit():
    year=int(year)
    if (year % 4 ==0 and year %100 != 0) or year % 400 ==0:
        print(year,"-високосный год")
    else:
        print("Год не високосный")   
else:
    print("Вы ввели не цифровое значение")         








