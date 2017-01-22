from autocorrect import spell
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re


#FUNCTIONS
def spell_check(word):
	if bool(re.search(r'\d', word)) or all(c.isupper() for c in word):
		return word
	else:
		return spell(word)

def clean(line, stop_words):
	tokens = word_tokenize(line)
	#sc_tokens = list(map(spell_check, tokens))
	filtered_sentence = [t for t in tokens if not t in stop_words]
	return ' '.join(filtered_sentence)





#SCRIPT
transcribed = open('transcript_CIA-RDP07X00001R000100010001-9.pdf.txt', 'rt', encoding='latin1')
spellchecked = open('spellchecked_CIA-RDP07X00001R000100010001-9.pdf.txt', 'w', encoding='latin1')

stop_words = set(stopwords.words('english'))

for line in transcribed:
	cleaned_line = clean(line, stop_words)
	try:
		spellchecked.write(cleaned_line + "\n")
	except UnicodeEncodeError:
		print(cleaned_line)
		continue

transcribed.close()
spellchecked.close()



