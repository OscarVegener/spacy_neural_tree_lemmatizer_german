import spacy

nlp = spacy.load('de_core_news_sm')

file = open('keywords.txt', 'r')
text = file.read()
file.close()

keywords = text.split(' ')

lemmas_file = open('./results/default_keyword_lemmas_res.txt', 'w')

for keyword in keywords:
    lemmas_file.write(f"{nlp(keyword)[0].lemma_}\n")

lemmas_file.close()
