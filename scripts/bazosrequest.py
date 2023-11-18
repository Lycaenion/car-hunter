import requests

html = requests.get("https://auto.bazos.sk/ford/?hledat=galaxy&rubriky=auto&hlokalita=97411&humkreis=300&cenaod=&cenado=&order=&crp=&kitx=ano").
print(html.text)git