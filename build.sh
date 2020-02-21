#!/bin/bash

printf "Training all...\n"
./train_script.sh
printf "Training char model...\n"
./train_char.sh
printf "Training words model...\n"
./train_word.sh
