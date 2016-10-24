#!/bin/bash

th sample.lua cv/word-rrn-trained.t7 \
	-gpuid -1 \
	-temperature .7 \
	-length 500 \
	-primetext "I will make America "
