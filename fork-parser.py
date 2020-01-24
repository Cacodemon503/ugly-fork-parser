import requests
import re 
import itertools 
from itertools import groupby 
import csv 
import time 

start = time.monotonic()

token = open('token.txt' , 'r').read()
headers = {'Authorization': 'token ' + token}

link = str(input('Paste URL: '))  
URL = link

r = requests.get(url = URL)
data = r.text 
results = re.findall(r"users/(.*?)/hovercard", data) 
results_clean = [el for el, _ in groupby(results)]  


with open('{}.txt'.format(str(input('Enter file name: '))), 'w', encoding="utf-8") as filename:
    writer = None 
    for username in results_clean:
        URL_2 = 'https://api.github.com/users/' + username
        r = requests.get(url = URL_2, headers=headers)
        data = r.json()
        readout = {'Username': data['login'], 'Full Name': data['name'], 'Email': data['email'],
                   'Location': data['location'], 'Company': data['company'], 'Hireable Status': data['hireable'],
                   'Profile Summary': 'https://profile-summary-for-github.com/user/' + data['login']}
        if not writer:
            writer = csv.DictWriter(filename, delimiter=';', fieldnames=readout.keys())
            
        writer.writerow(readout)
        
        
        print('Wrting ...')
        
print(str("Users parsed: ") + str(len(results_clean)))
print ('Writing completed')

result = time.monotonic() - start
print("Program time: " + str(result) + " seconds.")
