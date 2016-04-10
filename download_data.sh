wget https://dumps.wikimedia.org/tewiki/20160407/tewiki-20160407-pages-articles-multistream.xml.bz2
wget https://github.com/attardi/wikiextractor/raw/master/WikiExtractor.py

bzip2 -d tewiki-20160407-pages-articles-multistream.xml.bz2

python2 WikiExtractor.py -o data/ tewiki-20160407-pages-articles-multistream.xml