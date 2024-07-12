import requests

resp = requests.post("https://recomendacionusuarios-3bgweof3mq-uc.a.run.app", files={'file': open('eight.png', 'rb')})

print(resp.json())