import requests

resp = requests.post("https://prediccionexito-3bgweof3mq-uc.a.run.app",json={'stars': "4", 'review_count':"112", 'state':"IN"})

print(resp.json())