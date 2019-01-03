import re
import spacy
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from contraction import CONTRACTION_MAP
nlp = spacy.load('en_core', parse=True, tag=True, entity=True)
stopwords = nltk.corpus.stopwords.words('english')
stopwords.remove('no')
stopwords.remove('not')
tokenizer = ToktokTokenizer()


def remove_special(text):
    pattern = r'[^a-zA-z0-9/s]'
    text = re.sub(pattern, ' ', text)
    return text


def lemma(text):
    text = nlp(text)
    text = ' '.join([word.lemma_ if '-PRON' not in word.lemma_ else word.text for word in text])
    return text


def expand_contractions(text, contraction_mapping=CONTRACTION_MAP):
    contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())),
                                      flags=re.IGNORECASE | re.DOTALL)

    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contraction_mapping.get(match) \
            if contraction_mapping.get(match) \
            else contraction_mapping.get(match.lower())
        expanded_contraction = first_char + expanded_contraction[1:]
        return expanded_contraction

    expanded_text = contractions_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", " ", expanded_text)
    return expanded_text


def remove_stopwords(text):
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    filtered = [token for token in tokens if token.lower not in stopwords]
    filtered_text = ' '.join(filtered)
    return filtered_text

