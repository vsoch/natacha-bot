!# /bin/bash

th train.lua \
	-gpuid -1 \
	-data_dir data/trump  \
	-train_frac 0.96 \
	-val_frac 0.04 \
	-max_epochs 30 \
	-word_level 1 \
	-threshold 2 \
	-print_every 10 \
	-glove 1 \
	-rnn_size 128 \
	-num_layers 2 \
	-dropout 0.5 \
	# -recurrent_dropout 0.5 \
