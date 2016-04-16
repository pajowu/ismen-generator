import re
import json
import requests
from bs4 import BeautifulSoup
req = requests.get("https://de.wikipedia.org/wiki/-ismus")
page = BeautifulSoup(req.text)
data = page.getText('')
reg = r'\w+ismus'
matches = sorted(re.findall(reg, data))
with open("ismen-liste", "w", encoding="utf-8") as ismfile:
	json.dump(matches, ismfile)