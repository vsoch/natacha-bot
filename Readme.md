# Trump bot
Generates new speeches in Donald Trump's style using a [word-level RNN](https://github.com/larspars/word-rnn) and [pre-trained](http://nlp.stanford.edu/projects/glove/) glove word vectors.

## Usage
* Pull docker image: `docker pull rtlee/t-bot:dev`
* Run docker container: `docker run -t -i rtlee/t-bot:dev /bin/bash`
* Train model _(optional)_: `source train_script.sh`
* Sample from model: `th sample.lua cv/lm_lstm_epoch50.00_1.1925.t7 -temperature .4 -length 500 -gpuid -1 -primetext "The meaning of life is"`

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
