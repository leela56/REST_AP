import requests 
payload = {'page' : 2, 'count' : 25}

r = requests.get('https://http.org/get',params = payload)
print(r.url)