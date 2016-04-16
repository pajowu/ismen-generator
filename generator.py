import random
import json
with open("ismen-liste", encoding="utf-8") as ismfile:
	ismen = json.load(ismfile)
	ismus = random.choice(ismen).lower()
	print("anarcho-"+ismus)