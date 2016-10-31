class TestClass:

    # Read data
    with open("data/trump/input_raw.txt", "r") as f:
        data = f.read()
    words = data.split()
    word_count = len(words)

    def test_duplicate_speeches(self, phrase_len=100):
        duplicates_found = False
        for i in range(0, self.word_count - phrase_len):
            phrase = ' '.join(self.words[i: i + phrase_len])
            if self.data.count(phrase) > 1:
                duplicates_found = True
                print 'Found the following phrase multiple times {}'.\
                    format(phrase)
        assert not duplicates_found
