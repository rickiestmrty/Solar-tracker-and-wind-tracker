'''
Bunzel Building
LATITUDE = 10.35189
LONGITUDE = 123.91335

https://suncalc.org/#/lat,lon,zoom/date/time/objectlevel/maptype

useful links:
https://stackoverflow.com/questions/16180428/can-selenium-webdriver-open-browser-windows-silently-in-the-background
'''

import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup

class SunCalc:
    
    def __init__(self,lat,long) -> None:
        self.LATITUDE = lat
        self.LONGITUDE = long
        self.SITE = "https://suncalc.org/#/"

    def get_curr_datetime(self) -> list:
        current_datetime = datetime.datetime.now()
        date = current_datetime.strftime("%Y.%m.%d")
        time = current_datetime.strftime("%H:%M")
        return [date,time]

    def get_data(self,link) -> str:
        display = Display(visible=0, size=(800, 600))
        display.start()
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(link)
        content = driver.page_source
        soup = BeautifulSoup(content,"html.parser")
        a = str(soup.find("span", {"id": "azimuth"}))
        return a

    def get_link(self) -> str:
        datetime = self.get_curr_datetime()
        link = self.SITE + str(self.LATITUDE) + "," + str(self.LONGITUDE) + ",null/" + datetime[0] + "/" + datetime[1] + "/null/null"
        return link

    def get_angle(self) -> float:
        link = self.get_link()
        html_data = self.get_data(link)
        azmuth = float(html_data[32:37])
        return azmuth

hello = SunCalc(10.35189,123.91335).get_angle()
print(hello)