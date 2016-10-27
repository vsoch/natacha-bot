import sys
import subprocess
import random
import string


class Sampler():

    def __init__(self, seed_text=None,
                 char_temperature=.4, word_temperature=.75):
        # Generate random character for the seed if none provided
        if seed_text is None:
            seed_text = random.choice(string.letters).upper()
        self.seed = seed_text
        self.char_temperature = char_temperature
        self.word_temperature = word_temperature

    def get_sample_raw(self, model_type, seed, temperature, length):
        # Generate random character if none provided
        if seed is None:
            seed = random.choice(string.letters).upper()

        # Get model name
        if model_type == 'word':
            model_name = 'cv/word-rnn-trained.t7'
        elif model_type == 'char':
            model_name = 'cv/char-rnn-trained.t7'
        else:
            raise ValueError('Model type {} not supported'.format(model_type))

        # Sample from the model using provided seed
        sample = subprocess.check_output([
            'th', 'sample.lua',
            model_name,
            '-temperature', str(temperature),
            '-length', str(length),
            '-gpuid', '-1',
            '-primetext', seed
        ])

        # Return cleaned sampled text
        return self.denormalize(sample)

    # Denormalize sampled text
    def denormalize(self, sample):
        sample_clean = str(sample).split("--------------------------")[1]
        sample_clean = sample_clean.replace(" . . . ", "... ")
        sample_clean = sample_clean.\
            replace(" . ", ". ").\
            replace(" \ ? ", "? ").\
            replace(" ! ", "! ").\
            replace(" ' ", "'").\
            replace(" , ", ", ").\
            replace("- -", "--").\
            replace(" ; ", "; ")
        sample_clean = sample_clean.replace(" n't", "n't")
        return sample_clean

    def get_sample(self):
        if self.seed.strip()[-1:] != '.':
            char_sample = self.get_sample_raw(
                'char', self.seed, self.char_temperature, 300)
            char_sample_clean = ' '.join([
                word.replace(' ', '')
                for word in char_sample.split('   ')])
            if char_sample[0] != ' ':
                char_sample_clean = char_sample_clean.strip()
            sample_starter = self.seed + \
                char_sample_clean.split('.')[0] + '.'
        else:
            sample_starter = self.seed

        word_sample = self.get_sample_raw(
            'word', sample_starter, self.word_temperature, 500)
        sample_clean = sample_starter + ' ' + word_sample
        return ' '.join(sample_clean.split())

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sampler = Sampler(sys.argv[1])
    else:
        sampler = Sampler()
    print sampler.get_sample()
