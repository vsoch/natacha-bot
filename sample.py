import sys
import subprocess
import random
import string


def get_sample(seed_text=None):

    # Generate random character if none provided
    if seed_text is None:
        seed_text = random.choice(string.letters).upper()

    # Sample from the model using provided seed
    sample = subprocess.check_output([
        'th', 'sample.lua',
        'cv/word-rrn-trained.t7',
        '-temperature', '.75',
        '-length', '500',
        '-gpuid', '-1',
        '-primetext', seed_text
    ])

    # Return cleaned sampled text
    sample_clean = str(sample).split("--------------------------")[1]
    sample_clean = sample_clean.replace(" ' ", "'")
    sample_clean = sample_clean.replace(" .", ".").replace(" ?", "?").\
        replace(" !", "!").replace(" ,", ",").replace(" ;", ";")
    sample_clean = ' '.join(sample_clean.split())
    return seed_text.strip() + ' ' + sample_clean

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print get_sample(sys.argv[1])
    else:
        print get_sample()
