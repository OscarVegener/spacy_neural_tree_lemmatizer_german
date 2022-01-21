import stanza
import spacy_stanza

stanza.download("de")

nlp = spacy_stanza.load_pipeline("de")

file = open('article.txt')
text = file.read()
file.close()

doc = nlp(text)

lemmas_file = open('./results/stanza_article_lemmas_res.txt', 'w')

for token in doc:
    lemmas_file.write(f"{token.lemma_}\n")

lemmas_file.close()
