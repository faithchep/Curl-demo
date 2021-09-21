import requests
from requests.structures import CaseInsensitiveDict

url = "https://hiskenya.org/api/dataElementGroups/nc1L92Vuwy8"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Basic U2luamlyaTpPdHdlcm85Ni4="
headers["Cookie"] = "JSESSIONID=7566DEA3E3668BBB6FAB103EE05499F7"


resp = requests.get(url, headers=headers)

print(resp.text)

