# coding: utf-8
import re


def save_clean(file_name_in, file_name_out):
    with open(file_name_in, "r") as f:
        data = f.read()

    data_clean = clean_str(data)

    with open(file_name_out, "w") as text_file:
        text_file.write(data_clean)

    print "{} words from {} saved to {}.".format(
        len(data_clean.split()), file_name_in, file_name_out)


def clean_str(string):
    string = string.replace('’', '\'')
    string = string.replace('–', '\-')
    string = re.sub(r"[^가-힣A-Za-z0-9(),\;\-\.!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip()

if __name__ == '__main__':
    save_clean("input.txt", "input_norm_punctuation/input.txt")
