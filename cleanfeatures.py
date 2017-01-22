import csv

#returns 1 if the feature is in the list of keywords, 0 otherwise
def vectorize_helper(keywords, feature):
	if feature in keywords:
		return 1
	else:
		return 0

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

possible_features = []

for word in frequencies:
	if frequencies[word] > 3:
		possible_features.append(word)

i = 0
features = []
for feature in possible_features:
	try:
		print(feature)
		features.append(feature)
	except UnicodeEncodeError:
		i += 1
		continue;
print(i)

# with open('document_data.csv', 'w', newline="") as csvfile:
# 	writer = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 	for doc in all_data:
# 		keywords = doc[1].split(', ')
# 		vector = list(map(lambda feature: vectorize_helper(keywords, feature), features))
# 		writer.writerow(vector)

writer = open('document_data.dat', 'w')
for doc in all_data:
	keywords = doc[1].split(', ')
	vector = list(map(lambda feature: vectorize_helper(keywords, feature), features))
	for i in range (0, len(vector) - 1):
		writer.write(str(vector[i]))
		writer.write(', ')
	writer.write(str(vector[len(vector) - 1]))
	writer.write('\n')
writer.close()
