import spacy

nlp = spacy.load('de_core_news_sm')

file = open('article.txt')
text = file.read()
file.close()

doc = nlp(text)

lemmas_file = open('./results/default_article_lemmas_res.txt', 'w')

for token in doc:
    lemmas_file.write(f"{token.lemma_}\n")

lemmas_file.close()
