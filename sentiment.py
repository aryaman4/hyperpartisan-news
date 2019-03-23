from afinn import Afinn
from preprocess import *
af = Afinn()
s = "A tenant-driven class action #lawsuit brought against 2 Lower Manhattan buildings ravaged by #HurricaneSandy dismissed"
import spacy
nlp = spacy.load('en_core', parse=True, tag=True, entity=True)
sen = remove_special(s)
sentence = lemma(sen)
sentence = remove_stopwords(sentence)
sentence_nlp = nlp(sentence)

dependency_pattern = '{left}<---{word}[{w_type}]--->{right}\n--------'
orths = [token.orth_ for token in sentence_nlp]
left = []
right = []
keywords = ['subway', 'hurricanesandy', 'mta']
for token in sentence_nlp:
    left.append([t.orth_ for t in token.lefts])
    right.append([t.orth_ for t in token.rights])
print(orths)
print(left)
print(right)
score = 0
for i, t in enumerate(orths):
    if t in keywords:
        for l in left[i]:
            score += af.score(l)
        for r in right[i]:
            score += af.score(r)
for i, l in enumerate(left):
    for k in keywords:
        if k in l:
            score += af.score(orths[i])
            for r in right[i]:
                score += af.score(r)
            for elem in l:
                score += af.score(elem)
for i, r in enumerate(right):
    for k in keywords:
        if k in r:
            score += af.score(orths[i])
            for l in left[i]:
                score += af.score(l)
            for elem in r:
                score += af.score(elem)
print(score)
