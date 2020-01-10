import os

def get_whois(url):
    command = f"whois {url}"
    process = os.popen(command)
    result = str(process.read())
    return result

# print(get_whois("fb.com"))