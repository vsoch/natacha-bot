#!/bin/bash

th train.lua \
	-gpuid -1 \
	-data_dir data/trump/input_norm_caps \
	-max_epochs 60 \
	-print_every 25 \
	-rnn_size 256 \
	-num_layers 3 \
	-dropout 0.4 \
	-eval_val_every 2000 \
	-checkpoint_dir cv_char_caps_256_3
