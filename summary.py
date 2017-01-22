import raker
import os


rake = raker.Rake("SmartStopList.txt")
output = open("features.txt", 'w')
for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith(".txt") and not file == "SmartStoplist.txt" and not file == "Outputs.txt":
        output.write(file + "\t")
        keywords = rake.run(open(file, 'r', encoding = 'Latin 1').read())
        phrases = []
        totalKeywords = len(keywords)
        for pair in keywords[0:(int(totalKeywords))]:
            phrases.append(pair[0])
        phrases = map(lambda s: ' '.join(s.split('\n')), phrases)
        phrases = map(lambda s: ' '.join(s.split('-')), phrases)
        phrases = map(lambda s: ' '.join(s.split('\t')), phrases)
        for phrase in phrases:
            try:
                output.write(phrase + ', ')
            except UnicodeEncodeError:
                continue;
        #output.write(','.join(phrases))
        output.write("\n")
output.close()
