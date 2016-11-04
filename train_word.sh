#!/bin/bash

th train.lua \
	-gpuid -1 \
	-data_dir data/trump/input_norm_caps  \
	-train_frac 0.96 \
	-val_frac 0.04 \
	-max_epochs 40 \
	-word_level 1 \
	-threshold 2 \
	-print_every 10 \
	-glove 1 \
	-rnn_size 256 \
	-num_layers 2 \
	-dropout 0.4 \
	-eval_val_every 500 \
	-checkpoint_dir cv_word_caps_256_2
