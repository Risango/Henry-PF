import requests

resp = requests.post("https://recomendacionusuarios-3bgweof3mq-uc.a.run.app", json={'business_id': "ozYCV1L1ACTIZuds0eyQLw"})

print(resp.json())
