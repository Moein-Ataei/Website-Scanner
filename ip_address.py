import socket

def get_ip_address(url):
    ip = socket.gethostbyname(url)
    return ip

# print(get_ip_address('https://www.varzesh3.com'))
# print(get_ip_address('varzesh3.com'))