import json

data = json.loads(open("results/cts6.dev.tdgroup.com.json").read())

print(data["data"]["connection"]["checked_hostname"])

