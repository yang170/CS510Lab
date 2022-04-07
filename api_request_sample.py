# wget -O dblp.json --no-check-certificate "https://inex:qatc2011@guacamole.univ-avignon.fr/dblp1/_search?q=\"Digital assistant\"&size=1"
import requests
from requests.auth import HTTPBasicAuth
requests.urllib3.disable_warnings()

url = "https://guacamole.univ-avignon.fr/dblp1/_search?q=%22Digital%20assistant%22&size=10"
resp = requests.get(url, auth=HTTPBasicAuth('inex', 'qatc2011'), verify=False)
print(resp.content)