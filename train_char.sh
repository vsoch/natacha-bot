#!/bin/bash

th train.lua \
	-gpuid -1 \
	-data_dir data/trump  \
	-max_epochs 30 \
	-print_every 10 \
	-rnn_size 128 \
	-num_layers 2 \
	-dropout 0.4 \
	-eval_val_every 1000 \
