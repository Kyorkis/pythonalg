#n = input("Введите трехзначное целое число:")
#x = 1
#y = 0
#for i in n:
#	y += int(i)
#	if int(i) != 0:
#		x *= int(i)
 
#print("Сумма цифр:", y)
#print("Произведение цифр:", x)

#z = int(input("Введите трехзначное число:"))

#x=z//100
#z = z - x*100
#y=z//10
#p=z%10

#print("Сумма всех чисел между собой:",x+y+p)
#print("Произведение чисел между собой:",x*y*p)
#x = 5
#y = 6
#print("{} = {}".format(x,bin(x)))
#print("")
#print("{} = {}".format(y,bin(y)))
#print(bin(x & y))
#print(bin(x | y))
#print(bin(x ^ y))
#print(bin(x >> 2))	
#print(bin(x << 2))	

import requests
#r = requests.get('https://api.github.com/events')
#print(r)
#r = requests.post('https://api.github.com/events', data={'key','value'})
#print(r)

#payload={"key1":'value1','key2':'value2'}
#r = requests.post('http://httpbin.org/post',data=payload)
#print(r.text)

#payload_tuples=[('key1','value1'),('key1','value2')]
#r1=requests.post('http://httpbin.org/post', data = payload_tuples)
#payload_dict={'key1':['value1','value2']}
#r2=requests.post("http://httpbin.org/post",data=payload_dict)
#print(r1.text)

#url='http://httpbin.org/post'
#files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}

#r=requests.post(url,files=files)
#print(r.text)


#r=requests.get('http://httpbin.org/get')
#print(r.status_code != requests.codes.ok)


#bad_r=requests.get('http://httpbin.org/get')
#print(bad_r.status_code)
#print(bad_r.raise_for_status())
#r=requests.get('http://httpbin.org/get')
#print(r.headers)



#url="http://example.com/some/cookie/setting/url"
#r=requests.get(url)
#print(r.cookies['example_cookie_name'])

import xml.etree.ElementTree as ET
data=ET.Element('data')
items = ET.SubElement(data,'items')
item1 = ET.SubElement(item, 'item')
item2 = ET.SubElement(item, 'item')
item1.set('name','item1')
item2.set('name','item2')
item1.text='item1abc'
item2.text='item2abc'	