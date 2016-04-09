import regex
import glob
from bs4 import BeautifulSoup

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

