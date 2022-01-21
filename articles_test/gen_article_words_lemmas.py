import spacy

nlp = spacy.load('../training/UD_German-HDT/model-best')

file = open('article.txt')
text = file.read()
file.close()

doc = nlp(text)

lemmas_file = open('./results/article_lemmas_res.txt', 'w')

for token in doc:
    lemmas_file.write(f"{token.lemma_}\n")

lemmas_file.close()
