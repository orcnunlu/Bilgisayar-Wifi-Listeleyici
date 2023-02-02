import subprocess
import os
liste=[]

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:

         liste.append("{:<30}|{:<}".format(i, results[0]))


        except IndexError:
         liste.append("{:<30}|{:<}".format(i, ""))



    except subprocess.CalledProcessError:
         liste.append("{:<30}|  {:<}".format(i, "Çözümlenemedi"))

if os.path.exists('wifi.txt'):
        os.remove('wifi.txt')
for list in liste:
    with open('wifi.txt', 'a+', encoding='utf-8') as f:
        f.write(str(list+"\n"))
        f.close()