class Read:

    def frequency_map(self, text, k):
        """Identifies the combinations of nucleotides present in a sequence from a given k-mer value
        and adds them to a dictionary.

        Arguments:
            text, k

        Returns:
            freq

        """
        freq = {}
        n = len(text)
        for i in range(n-k+1):
            pattern = text[i: i+k]
            freq[pattern] = 0
            for j in range(n-k+1):
                if freq[pattern] == pattern:
                    freq[pattern] += 1
        return freq

    def frequency_words(self, text, k):
        words = []
        freq = self.frequency_map(text, k)
        m = max(freq.values())
        for key in freq:
            if freq[key] == m:
                words.append(key)
        return words
