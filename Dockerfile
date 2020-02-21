FROM rtlee/t-bot:train
# docker build -t natachabot .
# docker run natachabot "I want to"
COPY data/natacha/input.txt /root/Trump-bot/data/natacha/input.txt
COPY data/natacha/train_char.sh /root/Trump-bot/train_char.sh
COPY data/natacha/train_word.sh /root/Trump-bot/train_word.sh
COPY data/natacha/train_script.sh /root/Trump-bot/train_script.sh
COPY ./build.sh /root/Trump-bot/build.sh
RUN /bin/bash /root/Trump-bot/build.sh
RUN cp cv_char/lm_lstm_epoch30.00_1.3580.t7 cv/char-rnn-trained.t7 && \ 
    cp cv_word_caps_256_2/lm_lstm_epoch40.00_4.4779.t7 cv/word-rnn-trained.t7
ENTRYPOINT ["python", "/root/Trump-bot/sample.py"]
