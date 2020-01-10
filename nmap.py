import os

def get_nmap(option, ip):
    command = f"nmap {option} {ip}"
    process = os.popen(command)
    result = str(process.read())
    return result


# print(get_nmap('-F', 'localhost'))