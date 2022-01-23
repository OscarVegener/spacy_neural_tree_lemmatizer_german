import spacy

source_nlp = spacy.load('../training/UD_German-HDT/model-last')

# nlp.add_pipe("tagger", before="experimental_edit_tree_lemmatizer")

nlp = spacy.load('de_core_news_lg', disable=["lemmatizer", "ner"])

nlp.add_pipe('experimental_edit_tree_lemmatizer', source=source_nlp)

print(nlp.pipe_names)

file = open('article.txt')
text = file.read()
file.close()

doc = nlp(text)

lemmas_file = open('./results/article_lemmas_res.txt', 'w')

for token in doc:
    lemmas_file.write(f"{token.lemma_}\n")

lemmas_file.close()
