import json 
import requests
from pprint import pprint as pp
lst = open('links1.json', 'r') 
json_lst = json.load(lst)
results_lst = []
for link in json_lst:
    response = requests.get(link).text
    json_response = json.loads(response)
    wanted_data = json_response['results']
    results_lst = results_lst + wanted_data
    pp(len(results_lst))
    
json_out = json.dumps(results_lst)

with open ('results.json','w') as f:
    f.write(json_out)