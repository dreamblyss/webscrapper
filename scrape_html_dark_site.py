


import requests as req
import socks
import socket

URL = "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion"

TOR_PROXY = {'http':'socks5h://localhost:9050', 'https':'socks5h://localhost:9050'}
res = req.get(url=URL, proxies=TOR_PROXY)

if res.status_code == 200:
	html = res.content.decode()
	print(html)

else:
	print(f'Something went wrong for this {URL} with status code: {res.status_code}')