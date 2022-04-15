# ==========================
# Made by @jasiukiewicztymon
# ==========================

# import section
import sys
import requests
from bs4 import BeautifulSoup

# getting the first argument
URL = sys.argv[1]

def parse_html(html):
    elem = BeautifulSoup(html, features="html.parser")
    text = ''
    for e in elem.descendants:
        if isinstance(e, str):
            text += e.strip()
        elif e.name in ['br',  'p', 'h1', 'h2', 'h3', 'h4','tr', 'th']:
            text += '\n'
        elif e.name == 'li':
            text += '\n- '
    return text

if URL[0:8] != "https://" and URL[0:7] != "http://":
    URL = "https://" + URL

try:
    HTML = requests.get(url = URL).text.split("<body>")[1].split("</body>")[0]

    imagesSrcArr = []

    

    CMHTML = parse_html(HTML)
    print(CMHTML)
except:
    print("Error 404 - Page not find")
