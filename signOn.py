from webbot import Browser
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#input type for IBM
#https://cn.sterlingcommerce.com/login.jsp

class SignOn:
    def __init__(self, URL, whereToClick, username,typeOfUserName,password):
        self.URL = URL
        web = Browser()
        web.go_to(URL)
        web.type(username,into=typeOfUserName)
        web.click('NEXT', tag = 'span')
        web.type(password, into='password')
        web.click('NEXT', tag = 'span')
        web.click(whereToClick)

    def getAllTagsById(self, tagType):
        response = requests.get(self.URL)
        soup = BeautifulSoup(response.text,'html.parser')
        soup.find_all(tagType)
def main():
    IBM_Login = SignOn('https://cn.sterlingcommerce.com/login.jsp','Sign In','Cody.Vollrath@southwire.com','text','Xxtriggered_911xX@')
    IBM_Login.getAllTagsById('a')

main()