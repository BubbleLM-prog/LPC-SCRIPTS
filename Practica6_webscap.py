#!/usr/bin/env phyton3


from bs4 import BeautifulSoup
import requests

page = requests.get('https://es.wikipedia.org/wiki/Nmap')
soup = BeautifulSoup(page.content,"html.parser")
text = soup.find_all("p")
print("Se encontraron" , len(text))
print("Accedemos al parrafo [0]")
potext = text[0].getText()
print(potext)


