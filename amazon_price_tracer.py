import requests
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from win10toast import ToastNotifier

toaster = ToastNotifier()
search = input("Enter Product Name: ")
store = {}
search_lists = search.split()
amazon_link = "https://amazon.in"

url = amazon_link+'/s?k='+'+'.join(search_lists)+'&ref=nb_sb_noss'

#function
def tracker(random_header):
    url_open = requests.get(url,headers = random_header)
    soup = BeautifulSoup(url_open.content,'html.parser')
    tag = soup('span',{'class':'a-size-medium a-color-base a-text-normal'})
    tag_2 = soup('span',{'class':'a-price-whole'})
    for i,j in zip(tag,tag_2):
        if search.lower() in (i.text).lower():
            print("{} || price: {} Rs".format(i.text,j.text))
            store[str(i.text)]=j.text
            for a,b in store.items():
                if str(i.text)==a:
                    if j.text<b:
                        toaster.show_toast("Amazon Deal",i.text+" || Price"+j.text)

while True:
    user = UserAgent()
    randomHeader = {'User-Agent':str(user.random)}
    print('Tracking.....',time.asctime(time.localtime(time.time())))
    tracker(randomHeader)
    time.sleep(60*5) #5 minutes