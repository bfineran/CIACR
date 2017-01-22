import json

corpus = open('features.txt')
all_data = []
frequencies = {}

for doc in corpus:
	data = doc.split('\t')
	all_data.append(data)
	keywords = data[1].split(', ')
	for keyword in keywords:
		if keyword not in frequencies:
			frequencies[keyword] = 0
		frequencies[keyword] += 1

features = {}

for word in frequencies:
	if frequencies[word] > 1:
		features[word] = []

for doc in all_data:
	keywords = doc[1].split(', ')
	for keyword in keywords:
		if keyword in features:
			features[keyword].append(doc[0])

json_feats = json.dumps(features)

with open('features.json', 'w') as f:
  json.dump(json_feats, f, ensure_ascii=False)