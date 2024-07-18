import requests

resp = requests.post("http://127.0.0.1:5000/",json={'business_id': "tvQqqSi6qnwYGMTSYfjWQw"})

print(resp.json())