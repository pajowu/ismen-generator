import random
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--source', help="Source of isms", choices=["wiki_de", "wiki_en", "ism_book"], default="wiki_de")
args = parser.parse_args()

with open(args.source+".list", encoding="utf-8") as ismfile:
	isms = json.load(ismfile)
	ism = random.choice(isms).lower()
	print("anarcho-"+ism)