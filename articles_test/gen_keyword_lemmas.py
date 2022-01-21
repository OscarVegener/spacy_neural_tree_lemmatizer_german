import spacy

nlp = spacy.load('../training/UD_German-HDT/model-best')

file = open('keywords.txt', 'r')
text = file.read()
file.close()

keywords = text.split(' ')

lemmas_file = open('./results/keyword_lemmas_res.txt', 'w')

for keyword in keywords:
    lemmas_file.write(f"{nlp(keyword)[0].lemma_}\n")

lemmas_file.close()
