# ==========================
# Made by @jasiukiewicztymon
# ==========================

# import section

import os
from os import system
import sys
from requests import session
from rich.console import Console
from rich.markdown import Markdown
from requests_html import HTML, HTMLSession
import markdownify

# getting the first argument
if len(sys.argv) > 1:
    URL = sys.argv[1]
else:
    #exiting in case of invalid argument
    print("Invalid URL...")
    exit()

# verification of the url
if URL[0:8] != "https://" and URL[0:7] != "http://":
    URL = "https://" + URL

# ===============================================
# How the browser work ?
# It's very simple and it pass only in few moves 
#
# 1 . Getting the url with the execution argument
# 2 . Getting the website HTML content
# 3 . Translating it to MarkDown
# 4 . Printing formated website with ascii images
# ===============================================

# oppening the session
session = HTMLSession()
r = session.get(URL)

# getting the html code
body = r.html.find('body', first=True)
html = body.html

title = "Open in browser"

# printing the menu
print('𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘')
print(f"\u001b]8;;{URL}\u001b\\{title}\u001b]8;;\u001b\\" + '     url: ' + URL)
print('𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘\n\n')

# getting the html content to markdown content
h = markdownify.markdownify(html, heading_style="ATX")

with open('h.txt', 'w', encoding='utf-8') as f:
    f.write(h)

pl = h.split('\n')

type = 'null'

console = Console()

for l in pl:
    ## Reading the titles 
    if type == 'null':
        if l.startswith('# '):
            if len(l[2:]) > 0:
                t = ''
                for i in range(len(l[2:])):
                    t += ' '
                t += '                                    '
                console.print(t, style="bold black on white")

                console.print('                  ' + l[2:] + '                  ', style="bold black on white")

                console.print(t, style="bold black on white")

                console.print('\n')
        elif l.startswith('## '):
            if len(l[3:]) > 0:
                console.print('                  ' + l[3:] + '                  ', style="bold black on white")
                console.print('\n')
        elif l.startswith('### '):
            if len(l[4:]) > 0:
                console.print('            ' + l[4:] + '            ', style="bold black on white")
                console.print('\n')
        elif l.startswith('#### '):
            if len(l[5:]) > 0:
                console.print('            ' + l[5:] + '            ', style="bold black on white")
                console.print('\n')
        elif l.startswith('##### '):
            if len(l[6:]) > 0:
                console.print('      ' + l[6:] + '      ', style="bold black on white")
                console.print('\n')
        elif l.startswith('###### '):
            if len(l[7:]) > 0:
                console.print('      ' + l[7:] + '      ', style="bold black on white")
                console.print('\n')
