import raker
import sys
import urllib2
import re

url = sys.argv[1]

response = urllib2.urlopen(url)
html = str(response.read())

# print(html)
# sys.stdout.flush()


def clean_markup(text):
    brackets = re.compile('{{.*?}}')
    tags = re.compile('<.*?>')
    cleantext = re.sub(brackets, '', text)
    cleantext = re.sub(tags, '', cleantext)
    cleantext = cleantext.replace('[', '')
    cleantext = cleantext.replace(']', '')
    return cleantext


rake = raker.Rake("SmartStoplist.txt")
# print(html)
# sys.stdout.flush()

plaintext = clean_markup(html)
output = ""
keywords = rake.run(plaintext)
phrases = []
for pair in keywords:
    phrases.append(pair[0])
phrases = map(lambda s: ' '.join(s.split('\n')), phrases)
phrases = map(lambda s: ' '.join(s.split('-')), phrases)
phrases = map(lambda s: ' '.join(s.split('\t')), phrases)
for phrase in phrases:
    output += phrase
    output += ', '
    #print("Phrase")

print(output)
sys.stdout.flush()
