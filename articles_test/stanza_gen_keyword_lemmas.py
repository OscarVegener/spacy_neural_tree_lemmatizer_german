import stanza
import spacy_stanza

stanza.download("de")

nlp = spacy_stanza.load_pipeline("de")

file = open('keywords.txt', 'r')
text = file.read()
file.close()

keywords = text.split(' ')

lemmas_file = open('./results/stanza_keyword_lemmas_res.txt', 'w')

for keyword in keywords:
    lemmas_file.write(f"{nlp(keyword)[0].lemma_}\n")

lemmas_file.close()
