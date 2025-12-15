

#Importing libraries
import requests as req
from urllib.request import urlopen
import tldextract
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen


#Importing Stem libraries
from stem import Signal
from stem.control import Controller
import socks, socket


#Initiating Connection
with Controller.from_port(port=9051) as controller:
    controller.authenticate("16:872860B76453A77D60CA2BB8C1A7042072093276A3D701AD684053EC4C")
    controller.signal(Signal.NEWNYM)

'''
# TOR SETUP GLOBAL Vars
SOCKS_PORT = 9050  # TOR proxy port that is default from torrc, change to whatever torrc is configured to
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", SOCKS_PORT)
socket.socket = socks.socksocket
'''


#URL = "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion"
URL = "http://xhgua4xb2aepz3i54catidnhuibcr5foqsergywqkzknc3a6btqq7hid.onion"

TOR_PROXY = {'http':'socks5h://localhost:9050', 'https':'socks5h://localhost:9050'}

SOCKS_PORT = 9050  # TOR proxy port that is default from torrc, change to whatever torrc is configured to
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", SOCKS_PORT)
socket.socket = socks.socksocket


# Perform DNS resolution through the socket
def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

socket.getaddrinfo = getaddrinfo

URL = "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion"

TOR_PROXY = {'http':'socks5h://localhost:9050', 'https':'socks5h://localhost:9050'}

KEYWORDS = ['software', 'Malware', 'STYX', 'Exodus', 'Cypher', 'Exploit',  'Ransomware', 'Hacking', 'Fullz' 
'BINs', 'RDP', 'VDS', 'Data', 'dumps',  'Credentials', 'PII', 'Credit', 'cards', 'Stolen', 'data',
'Cypher', 'Crypt', 'forums', 'Cyberattack', 'Cybercriminal', 'images', '<a>']



def scrap(URL):

    res = req.get(url=URL,proxies=TOR_PROXY)

    if res.status_code == 200:
    #pass
        html = res.content.decode()

        for keyword in KEYWORDS:
            if keyword in html.lower():
                print(f'"{keyword}" found in {URL}.')


    #print(html)
    else:
        print(f'Something went wrong for this {URL} with status code: {res.status_code}')

def scrap_from_file(PATH):
    with open(PATH) as f:
        
        links = f.readlines()
        links = [link.replace('\n', '') for link in links]

        for link in links:
            scrap(link)

if __name__ == '__main__':
 #scrap(URL)
   scrap_from_file(r'lnk.txt')