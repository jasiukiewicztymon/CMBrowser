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
print('\n')
print(f"\u001b]8;;{URL}\u001b\\{title}\u001b]8;;\u001b\\" + '     url: ' + URL)
print('𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘𝄘')
print('\n')

def href(title, url):
    return f"\u001b]8;;{url}\u001b\\{title}\u001b]8;;\u001b\\"

# getting the html content to markdown content
h = markdownify.markdownify(html, heading_style="ATX")

with open('h.txt', 'w', encoding='utf-8') as f:
    f.write(h)

pl = h.split('\n')

tmp = ''

console = Console()

for l in pl:
    l = l.strip()
    if tmp != '':
        if len(l) > 0:
            if l[-1] == ')' and l.find('](') != -1:
                l = tmp + ' ' + l
            else:
                l, tmp = tmp, l

                # Start

                if l.startswith('* '):
                    l = l[2:]
                    if l[0] == '[' and l[-1] == ')' and l.find('](') != -1:
                        l = href(l[1:(l.find(']'))], l[(l.find('(')+1):-1])
                        console.print('🔵 ' + l)
                    elif l.startswith('![') and l[-1] == ')' and l.find('](') != -1:
                        console.print('\t🔹 <img>')
                    else:
                        l = '🔵 ' + l
                        console.print(Markdown(l))
                elif l.startswith('+ '):
                    l = l[2:]
                    if l[0] == '[' and l[-1] == ')' and l.find('](') != -1:
                        l = href(l[0:(l.find(']'))], l[(l.find('(')+1):-1])
                        console.print('\t🔹 ' + l)
                    elif l.startswith('![') and l[-1] == ')' and l.find('](') != -1:
                        console.print('\t🔹 <img>')
                    else:
                        print('\t🔹 ', end='')
                        console.print(Markdown(l))
                        console.print('\033[1A\033[1A')

                # Separator
                elif l == '***' or l == '---':
                    print('')
                    console.print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', style="bold black on white")
                    print('')

                # Headers
                elif l.startswith('# '):
                    l = l[2:]
                    if len(l) > 0:
                        console.print('\n')
                        if len(l) >= 6:
                            if l[0] == '[' and l[-1] == ')' and l.find(']') != -1 and l.find('(') != -1:
                                console.print('      ' + l[1:(l.find(']') - 1)] + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', style="bold black on white")
                                l = href(l[1:(l.find(']') - 1)], l[(l.find('(')+1):-1])
                                console.print('\n')
                                l = '            ▶ ' + l
                                console.print(l, style="bold")
                                console.print('\n')
                            else:
                                u = len(l)
                                l = '      ' + l + ' : '
                                t = ''
                                for _ in range(250 - u):
                                    t += ' '

                                console.print(l + t, style="bold black on white")
                                console.print('\n')
                        else:
                            u = len(l)
                            l = '      ' + l + ' : '
                            t = ''
                            for _ in range(250 - u):
                                t += ' '

                            console.print(l + t, style="bold black on white")
                            console.print('\n')
                elif l.startswith('## '):
                    l = l[3:]
                    if len(l) > 0:
                        console.print('\n')
                        if len(l) >= 6:
                            if l[0] == '[' and l[-1] == ')' and l.find(']') != -1 and l.find('(') != -1:
                                console.print('      ' + l[1:(l.find(']') - 1)] + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', style="bold black on white")
                                l = href(l[1:(l.find(']') - 1)], l[(l.find('(')+1):-1])
                                console.print('\n')
                                l = '            ▶ ' + l
                                console.print(l, style="bold")
                            else:
                                u = len(l)
                                l = '      ' + l + ' : '
                                t = ''
                                for _ in range(250 - u):
                                    t += ' '

                                console.print(l + t, style="bold black on white")
                                console.print('\n')
                        else:
                            u = len(l)
                            l = '      ' + l + ' : '
                            t = ''
                            for _ in range(250 - u):
                                t += ' '

                            console.print(l + t, style="bold black on white")
                            console.print('\n')
                elif l.startswith('### '):
                    l = l[4:]
                    if len(l) > 0:
                        console.print('\n')
                        if len(l) >= 6:
                            if l[0] == '[' and l[-1] == ')' and l.find(']') != -1 and l.find('(') != -1:
                                console.print('            ' + l[1:(l.find(']') - 1)] + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', style="bold black on white")
                                l = href(l[1:(l.find(']') - 1)], l[(l.find('(')+1):-1])
                                console.print('\n')
                                l = '            ▶ ' + l
                                console.print(l, style="bold")
                                console.print('\n')
                            else:
                                u = len(l)
                                l = '            ' + l + ' : '
                                t = ''
                                for _ in range(250 - u):
                                    t += ' '

                                console.print(l + t, style="bold black on white")
                                console.print('\n')
                        else:
                            u = len(l)
                            l = '            ' + l + ' : '
                            t = ''
                            for _ in range(250 - u):
                                t += ' '

                            console.print(l + t, style="bold black on white")
                            console.print('\n')
                elif l.startswith('#### '):
                    l = l[5:]
                    if len(l) > 0:
                        console.print('\n')
                        if len(l) >= 6:
                            if l[0] == '[' and l[-1] == ')' and l.find(']') != -1 and l.find('(') != -1:
                                console.print('            ' + l[1:(l.find(']') - 1)] + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', style="bold black on white")
                                l = href(l[1:(l.find(']') - 1)], l[(l.find('(')+1):-1])
                                console.print('\n')
                                l = '            ▶ ' + l
                                console.print(l, style="bold")
                                console.print('\n')
                            else:
                                u = len(l)
                                l = '            ' + l + ' : '
                                t = ''
                                for _ in range(250 - u):
                                    t += ' '

                                console.print(l + t, style="bold black on white")
                                console.print('\n')
                        else:
                            u = len(l)
                            l = '            ' + l + ' : '
                            t = ''
                            for _ in range(250 - u):
                                t += ' '

                            console.print(l + t, style="bold black on white")
                            console.print('\n')
                elif l.startswith('##### '):
                    l = l[6:]
                    if len(l) > 0:
                        console.print('\n')
                        if len(l) >= 6:
                            if l[0] == '[' and l[-1] == ')' and l.find(']') != -1 and l.find('(') != -1:
                                console.print('                  ' + l[1:(l.find(']') - 1)] + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', style="bold black on white")
                                l = href(l[1:(l.find(']') - 1)], l[(l.find('(')+1):-1])
                                console.print('\n')
                                l = '            ▶ ' + l
                                console.print(l, style="bold")
                                console.print('\n')
                            else:
                                u = len(l)
                                l = '                  ' + l + ' : '
                                t = ''
                                for _ in range(250 - u):
                                    t += ' '

                                console.print(l + t, style="bold black on white")
                                console.print('\n')
                        else:
                            u = len(l)
                            l = '                  ' + l + ' : '
                            t = ''
                            for _ in range(250 - u):
                                t += ' '

                            console.print(l + t, style="bold black on white")
                            console.print('\n')
                elif l.startswith('###### '):
                    l = l[7:]
                    if len(l) > 0:
                        console.print('\n')
                        if len(l) >= 6:
                            if l[0] == '[' and l[-1] == ')' and l.find(']') != -1 and l.find('(') != -1:
                                console.print('                  ' + l[1:(l.find(']') - 1)] + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', style="bold black on white")
                                l = href(l[1:(l.find(']') - 1)], l[(l.find('(')+1):-1])
                                console.print('\n')
                                l = '            ▶ ' + l
                                console.print(l, style="bold")
                                console.print('\n')
                            else:
                                u = len(l)
                                l = '                  ' + l + ' : '
                                t = ''
                                for _ in range(250 - u):
                                    t += ' '

                                console.print(l + t, style="bold black on white")
                                console.print('\n')
                        else:
                            u = len(l)
                            l = '                  ' + l + ' : '
                            t = ''
                            for _ in range(250 - u):
                                t += ' '

                            console.print(l + t, style="bold black on white")
                            console.print('\n')

                # Links and images
                elif len(l) >= 4:
                    if l.startswith('[!') and l[-1] == ')' and l.find('](') != -1:
                        print('img')
                    elif l.startswith('[') and l[-1] == ')' and l.find('](') != -1:
                        l = href(l[1:(l.find(']'))], l[(l.find('(')+1):-1])
                        console.print(l)
                    elif l.startswith('![') and l[-1] == ')' and l.find('](') != -1:
                        l = href(l[2:(l.find(']'))], l[(l.find('(')+1):-1])
                        console.print(l)
                    else:
                        if len(l) > 1:
                            console.print(Markdown(l))
                else:
                    if len(l) > 1:
                        console.print(Markdown(l))

                # End

                l, tmp = tmp, l

            tmp = ''
    if tmp == '':
        # Lists
        if len(l) > 0:
            if l[0] == '[' and l[-1] != ')':
                tmp = l
            elif l.startswith('* '):
                l = l[2:]
                if l[0] == '[![' and l[-1] == ')' and l.find('](') != -1:
                    #image
                    console.print('🔵 ' + l)
                elif l.startswith('![') and l[-1] == ')' and l.find('](') != -1:
                    console.print('\t🔹 <img>')
                else:
                    l = '🔵 ' + l
                    console.print(Markdown(l))
            elif l.startswith('+ '):
                l = l[1:]
                if l[0] == '[![' and l[-1] == ')' and l.find('](') != -1:
                    # image
                    console.print('\t🔹 ' + l)
                if l.startswith('![') and l[-1] == ')' and l.find('](') != -1:
                    console.print('\t🔹 <img>')
                else:
                    print('\t🔹 ', end='')
                    console.print(Markdown(l))
                    console.print('\033[1A\033[1A')

            # Separator
            elif l == '***' or l == '---':
                print('')
                console.print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', style="bold black on white")
                print('')

            # Headers
            elif l.startswith('# '):
                l = l[2:]
                if len(l) > 0:
                    console.print('\n')
                    if len(l) >= 6:
                        if l[0] == '[' and l[-1] == ')' and l.find(']') != -1 and l.find('(') != -1:
                            console.print('      ' + l[1:(l.find(']') - 1)] + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', style="bold black on white")
                            l = href(l[1:(l.find(']') - 1)], l[(l.find('(')+1):-1])
                            console.print('\n')
                            l = '            ▶ ' + l
                            console.print(l, style="bold")
                            console.print('\n')
                        else:
                            u = len(l)
                            l = '      ' + l + ' : '
                            t = ''
                            for _ in range(250 - u):
                                t += ' '

                            console.print(l + t, style="bold black on white")
                            console.print('\n')
                    else:
                        u = len(l)
                        l = '      ' + l + ' : '
                        t = ''
                        for _ in range(250 - u):
                            t += ' '

                        console.print(l + t, style="bold black on white")
                        console.print('\n')
            elif l.startswith('## '):
                l = l[3:]
                if len(l) > 0:
                    console.print('\n')
                    if len(l) >= 6:
                        if l[0] == '[' and l[-1] == ')' and l.find(']') != -1 and l.find('(') != -1:
                            console.print('      ' + l[1:(l.find(']') - 1)] + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', style="bold black on white")
                            l = href(l[1:(l.find(']') - 1)], l[(l.find('(')+1):-1])
                            console.print('\n')
                            l = '            ▶ ' + l
                            console.print(l, style="bold")
                        else:
                            u = len(l)
                            l = '      ' + l + ' : '
                            t = ''
                            for _ in range(250 - u):
                                t += ' '

                            console.print(l + t, style="bold black on white")
                            console.print('\n')
                    else:
                        u = len(l)
                        l = '      ' + l + ' : '
                        t = ''
                        for _ in range(250 - u):
                            t += ' '

                        console.print(l + t, style="bold black on white")
                        console.print('\n')
            elif l.startswith('### '):
                l = l[4:]
                if len(l) > 0:
                    console.print('\n')
                    if len(l) >= 6:
                        if l[0] == '[' and l[-1] == ')' and l.find(']') != -1 and l.find('(') != -1:
                            console.print('            ' + l[1:(l.find(']') - 1)] + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', style="bold black on white")
                            l = href(l[1:(l.find(']') - 1)], l[(l.find('(')+1):-1])
                            console.print('\n')
                            l = '            ▶ ' + l
                            console.print(l, style="bold")
                            console.print('\n')
                        else:
                            u = len(l)
                            l = '            ' + l + ' : '
                            t = ''
                            for _ in range(250 - u):
                                t += ' '

                            console.print(l + t, style="bold black on white")
                            console.print('\n')
                    else:
                        u = len(l)
                        l = '            ' + l + ' : '
                        t = ''
                        for _ in range(250 - u):
                            t += ' '

                        console.print(l + t, style="bold black on white")
                        console.print('\n')
            elif l.startswith('#### '):
                l = l[5:]
                if len(l) > 0:
                    console.print('\n')
                    if len(l) >= 6:
                        if l[0] == '[' and l[-1] == ')' and l.find(']') != -1 and l.find('(') != -1:
                            console.print('            ' + l[1:(l.find(']') - 1)] + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', style="bold black on white")
                            l = href(l[1:(l.find(']') - 1)], l[(l.find('(')+1):-1])
                            console.print('\n')
                            l = '            ▶ ' + l
                            console.print(l, style="bold")
                            console.print('\n')
                        else:
                            u = len(l)
                            l = '            ' + l + ' : '
                            t = ''
                            for _ in range(250 - u):
                                t += ' '

                            console.print(l + t, style="bold black on white")
                            console.print('\n')
                    else:
                        u = len(l)
                        l = '            ' + l + ' : '
                        t = ''
                        for _ in range(250 - u):
                            t += ' '

                        console.print(l + t, style="bold black on white")
                        console.print('\n')
            elif l.startswith('##### '):
                l = l[6:]
                if len(l) > 0:
                    console.print('\n')
                    if len(l) >= 6:
                        if l[0] == '[' and l[-1] == ')' and l.find(']') != -1 and l.find('(') != -1:
                            console.print('                  ' + l[1:(l.find(']') - 1)] + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', style="bold black on white")
                            l = href(l[1:(l.find(']') - 1)], l[(l.find('(')+1):-1])
                            console.print('\n')
                            l = '            ▶ ' + l
                            console.print(l, style="bold")
                            console.print('\n')
                        else:
                            u = len(l)
                            l = '                  ' + l + ' : '
                            t = ''
                            for _ in range(250 - u):
                                t += ' '

                            console.print(l + t, style="bold black on white")
                            console.print('\n')
                    else:
                        u = len(l)
                        l = '                  ' + l + ' : '
                        t = ''
                        for _ in range(250 - u):
                            t += ' '

                        console.print(l + t, style="bold black on white")
                        console.print('\n')
            elif l.startswith('###### '):
                l = l[7:]
                if len(l) > 0:
                    console.print('\n')
                    if len(l) >= 6:
                        if l[0] == '[' and l[-1] == ')' and l.find(']') != -1 and l.find('(') != -1:
                            console.print('                  ' + l[1:(l.find(']') - 1)] + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', style="bold black on white")
                            l = href(l[1:(l.find(']') - 1)], l[(l.find('(')+1):-1])
                            console.print('\n')
                            l = '            ▶ ' + l
                            console.print(l, style="bold")
                            console.print('\n')
                        else:
                            u = len(l)
                            l = '                  ' + l + ' : '
                            t = ''
                            for _ in range(250 - u):
                                t += ' '

                            console.print(l + t, style="bold black on white")
                            console.print('\n')
                    else:
                        u = len(l)
                        l = '                  ' + l + ' : '
                        t = ''
                        for _ in range(250 - u):
                            t += ' '

                        console.print(l + t, style="bold black on white")
                        console.print('\n')

            # Links and images
            elif len(l) >= 4:
                if l.startswith('[!') and l[-1] == ')' and l.find('](') != -1:
                    print('img')
                elif l.startswith('[') and l[-1] == ')' and l.find('](') != -1:
                    l = href(l[1:(l.find(']'))], l[(l.find('(')+1):-1])
                    console.print(l)
                elif l.startswith('![') and l[-1] == ')' and l.find('](') != -1:
                    l = href(l[2:(l.find(']'))], l[(l.find('(')+1):-1])
                    console.print(l)
                else:
                    if len(l) > 1:
                        console.print(Markdown(l))
            else:
                if len(l) > 1:
                    console.print(Markdown(l))

print('\n\n')
