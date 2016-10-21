!# /bin/bash

wget http://nlp.stanford.edu/data/glove.6B.zip
unzip glove.6B.zip
mkdir util/glove
cp glove.6B.200d.txt util/glove/vectors.6B.200d.txt
