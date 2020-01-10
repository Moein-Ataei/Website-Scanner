# import urllib.request
import requests

def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'

    req = requests.get(path + 'robots.txt')
    return req.text

# print(get_robots_txt("https://www.fb.com"))
