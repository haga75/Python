# cd /Json before running for correct file path

import json

with open("okidata.json", "r") as jsonfile:
    printerdata = json.load(jsonfile)

for group in printerdata["Device"]["BreadcrumbGroups"]:
    print(" - " + group["Name"])
