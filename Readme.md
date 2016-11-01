# Trump bot
Generates new speeches in Donald Trump's style using a [word-level RNN](https://github.com/larspars/word-rnn) and [pre-trained](http://nlp.stanford.edu/projects/glove/) glove word vectors.

## Usage
* Pull docker image: `docker pull rtlee/t-bot:dev`
* Run docker container: `docker run -t -i rtlee/t-bot:dev /bin/bash`
* Optional
	* Train model: `source train_script.sh`
	* Update model: `WIP`
* Sample from model: `python sample.py "I am going to"`

## To do
* [ ] Add recent speeches
* [ ] Remove speech delimiters
* [ ] Optimize RNN
* [ ] Incorporate paragraph vector?

## Credits, inspiration and similar projects
This is a fork of Lars Hiller Eidnes' [word-rnn](https://github.com/larspars/word-rnn), which is based on Andrej Karpathy's [char-rnn](https://github.com/karpathy/char-rnn).

* [Auto-Generating Clickbait With Recurrent Neural Networks](https://larseidnes.com/2015/10/13/auto-generating-clickbait-with-recurrent-neural-networks/)
* [DeepDrumpf](https://www.csail.mit.edu/deepdrumpf)
* [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
* [RoboTrumpDNN: Generating Donald Trump Speeches with Word2Vec and LSTM](https://github.com/ppramesi/RoboTrumpDNN)
