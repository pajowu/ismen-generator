import re
import json
import requests
from bs4 import BeautifulSoup
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--source', help="Source of isms", choices=["wiki_de", "wiki_en", "ism_book"], default="wiki_de")
args = parser.parse_args()

if args.source == "wiki_de":
	req = requests.get("https://de.wikipedia.org/wiki/-ismus")
elif args.source == "wiki_en":
	req = requests.get("https://en.wikipedia.org/wiki/Glossary_of_philosophy")
elif args.source == "ism_book":
	req = requests.get("http://www.ismbook.com/ismlist.html")

page = BeautifulSoup(req.text)
data = page.getText(' ')
reg = r'\w+ism(?:us)?'
matches = sorted(re.findall(reg, data))
with open(args.source+".list", "w", encoding="utf-8") as ismfile:
	json.dump(matches, ismfile)