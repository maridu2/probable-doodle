import requests

payload = {'apikey': '2505b789', 't': input('Título: ')}

r = requests.get('http://www.omdbapi.com/', params=payload)

response = r.json()

if not 'imdbID' in response:
    print('Comprueba tu ortografía, y ya que estás también tu inteligencia, imbécil, no sabes ni el nombre de la peli que quieres ver')
    exit()

imdbID = response['imdbID']
link = 'https://qazwsxedcrfvtgb.info/movie/' + imdbID

w = requests.get(link)

response = w.json()

streams = response['episodes'][0]['streams']

list = []
for stream in streams:
    list.append(stream['stream'])

list.reverse()

print(list)
