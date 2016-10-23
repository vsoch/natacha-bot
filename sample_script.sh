#!/bin/bash

th sample.lua cv/lm_lstm_epoch30.00_3.7313.t7 \
	-gpuid -1 \
	-temperature .7 \
	-length 500 \
	-primetext "I will make America "
