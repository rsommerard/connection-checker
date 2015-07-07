import urllib.request
import time

hostname = 'https://www.google.fr/'

while True:
    try:
        response = urllib.request.urlopen(hostname)
        print(time.strftime("[%H:%M:%S] Connection is back !"))
        print('\a') # Make a bip system
    except:
        print(time.strftime("[%H:%M:%S] Connection lost."))
        time.sleep(60)
