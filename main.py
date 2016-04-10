from read_data import wiki_sentences
import gensim, logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = gensim.models.Word2Vec(wiki_sentences())
model.save('w2vec_telugu')


for x in model.most_similar(positive=['కృష్ణా','మచిలీపట్నం'], negative=['ప్రకాశం']):
	print(x)