import regex

class regex_tokenizer():
    """
    Splits text based on regex patten.
    """

    def __init__(self, pattern, flags=0, gaps=False):
        self.pattern = pattern
        self._gaps = gaps
        self._flags = flags
        self._regexp = regex.compile(self.pattern, flags=self._flags)

    def tokenize(self, text):
        if self._gaps:
            return [tok for tok in self._regexp.split(text) if tok] #discard empty tokens
        else:
            return self._regexp.findall(text)


class sentence_tokenizer(regex_tokenizer):
    """
    Splits text into sentences based on punctuations.
    Decimals are taken care of.
    """
    #TODO: better tokenizer for abbreviations. Punkt tokenizer?

    # regex from here with some modifications: 
    # http://stackoverflow.com/questions/12683201/python-re-split-to-split-by-spaces-commas-and-periods-but-not-in-cases-like
    def __init__(self):
        regex_tokenizer.__init__(self, '(?<!\d)[\.]|[\.](?!\d)', gaps=True)


class word_tokenizer(regex_tokenizer):
    """
    Splits text into sentences based on punctuations.
    Decimals are taken care of.
    """
    def __init__(self):
        regex_tokenizer.__init__(self, r'[\d\.]+|\w+|[^\w\s]+', flags=regex.U)