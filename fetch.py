from bs4 import BeautifulSoup
from selenium import webdriver

URL = 'https://what-to-code.com/random'

def store(cardTitle, cardDesc):
    global cardData

    cardData = {
        'title': cardTitle,
        'desc': cardDesc
    }

def fetch():
    driver = webdriver.Chrome()
    driver.get(URL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    cardContent = soup.find('div').find('section').find('div').find('div').find_all('div')[1].find('div').find('div')
    cardTitle = cardContent.find_all('p')[0]
    cardDesc = cardContent.find_all('p')[1]
    store(cardTitle.text, cardDesc.text)

fetch()