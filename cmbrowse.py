# ==========================
# Made by @jasiukiewicztymon
# ==========================

# import section
import sys

from requests import session
from rich.console import Console
from rich.markdown import Markdown
from requests_html import HTML, HTMLSession

# getting the first argument
if len(sys.argv) > 1:
    URL = sys.argv[1]
else:
    print("Invalid URL...")
    exit()

if URL[0:8] != "https://" and URL[0:7] != "http://":
    URL = "https://" + URL

if len(sys.argv) > 1:
    session = HTMLSession()
    r = session.get(URL)

    body = r.html.find('body', first=True)
    html = body.html

    text = "This is a link"
    target = "http://example.com"
    print(f"\u001b]8;;{target}\u001b\\{text}\u001b]8;;\u001b\\")
else:
    print("Error 001: Invalid URL argument")
