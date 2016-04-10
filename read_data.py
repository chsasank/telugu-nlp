import regex
import glob
from bs4 import BeautifulSoup
from utils import sentence_tokenizer, word_tokenizer
import numpy as np
#TODO: Allow users to select the language  


def clean_text(text):
    """
    Removes contigous parts with 20 or more non telugu characters.
    This cleans spam.
    """
    return regex.sub('[^\p{Telugu}]{20,}', '', text)


def doc_generator():
    all_doc_files = sorted(glob.glob('data/*/wiki_*'))
    for file in all_doc_files:
        file_text = open(file, 'r').read()
        file_bs = BeautifulSoup(file_text)

        file_docs = file_bs.findAll('doc')
        for doc in file_docs:
            if doc['title'].find(':') == -1: #ignore meta pages
                yield clean_text(doc.contents[0])


class wiki_sentences(object):
    def __init__(self, num_docs=np.inf):
        self.sent_tok = sentence_tokenizer()
        self.tok = word_tokenizer()
        self.num_docs = num_docs

    def __iter__(self):
        docs = doc_generator()
        for i, doc in enumerate(docs):
            if i > self.num_docs: break
            for sent in self.sent_tok.tokenize(doc):
                yield self.tok.tokenize(sent)


if __name__ == '__main__':
    with open("data/all_articles.txt", "w") as myfile:
        for i, doc in enumerate(doc_generator()):
            myfile.write(doc)

            if i%100 == 0: print("Processed {} articles".format(i))

