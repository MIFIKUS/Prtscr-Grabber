import requests
import os
from urllib.request import urlretrieve
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time


# Увеличить скорость работы
# добавить список неработающих ссылок и сделать чтобы после except скрипт не начинался заново


#папка в которую по дефолту сохранять файлы
default = r'C:\\PrtscrGrabber\\'
#время паузы между переходом по ссылкам
time = 0.3

DRIVER = 'phantomjs.exe'
driver = webdriver.PhantomJS(DRIVER)



storage = input("Куда вы хотите сохранить скриншоты? ")
if storage == r"default":
    storage = default
    if not os.path.exists(default):
        os.makedirs(default)
        
# для того что бы не было вылетов при поиске ссылок
base_url = 'https://prnt.sc/'
base_headers = {'accept': '*/*',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
base_session = requests.Session()
base_request = base_session.get(base_url, headers=base_headers)
base_soup = bs(base_request.content, "html.parser")

DICT = ("a", "b", "c", "d",
        "e", "f", "g", "h",
        "i", "j", "k", "l",
        "m", "n", "o", "p",
        "q", "r", "s", "t",
        "u", "v", "w", "x",
        "y", "z", "0", "1",
        "2", "3", "4", "5",
        "6", "7", "8", "9")

headers = {
    'accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}

def link_brute(url, dictionary):
    session = requests.Session()
    num = 0
    # составление ссылки

    for link_5 in dictionary:
        symbol_5 = str(link_5)
        for link_4 in dictionary:
            symbol_4 = str(link_4)
            for link_3 in dictionary:
                symbol_3 = str(link_3)
                for link_2 in dictionary:
                    symbol_2 = str(link_2)
                    for link_1 in dictionary:
                        symbol_1 = str(link_1)
                        for link_0 in dictionary:
                            try:
                                symbol_0 = str(link_0)
                                # сборка ссылки с последнего символа
                                url_end = (symbol_5 + symbol_4 +
                                           symbol_3 + symbol_2 +
                                           symbol_1 + symbol_0)



                                ready_url = url + str(url_end)

                                request = session.get(ready_url, headers=headers)

                                if request.status_code == 200:
                                    soup = bs(request.content, "html.parser")
                                    # проверка на вылет на основной сайт
                                    if soup != base_soup:
                                        images = soup.find('img', attrs={'class': 'no-click screenshot-image'})
                                        # проверка на пустую картинку
                                        if images['src'] == '//st.prntscr.com/2019/04/03/1355/img/0_173a7b_211be8ff.png':
                                            continue
                                        else:
                                            if "https://image.prntscr.com/image/" in images['src']:
                                                print("№" + str(num) + " URL: " + ready_url + "           " + "Image URL: " + images['src'])
                                                driver.get(images['src'])
                                                screenshot = driver.save_screenshot(storage + str(num) + ".png")
                                                __import__('time').sleep(time)
                                            else:
                                                print("№" + str(num) + " URL: " + ready_url + "           " + "Image URL: " + images['src'])
                                                urlretrieve(images['src'], storage + str(num) + '.png')
                                                num += 1
                                                __import__('time').sleep(time)

                                    else:
                                        continue
                            except Exception:
                                pass



link_brute(base_url, DICT)

