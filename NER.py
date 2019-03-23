import spacy
nlp = spacy.load('en_core', parse=True, tag=True, entity=True)
from spacy import displacy

sentence = input()
sentence_nlp = nlp(sentence)

# print named entities in article
print([(word, word.ent_type_) for word in sentence_nlp if word.ent_type_])

# visualize named entities
displacy.render(sentence_nlp, style='ent', jupyter=True)