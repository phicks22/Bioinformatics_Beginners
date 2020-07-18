class Read:

    def frequency_map(self, text, k):
        """Identifies the combinations of adjacent nucleotides present in a sequence from a given k-mer value
        and adds them to a dictionary.

        Arguments:
            text, k

        Returns:
            freq

        """
        freq = {}
        n = len(text)
        for i in range(n - k + 1):
            pattern = text[i: i + k]
            freq[pattern] = 0
            for j in range(n - k + 1):
                if freq[pattern] == pattern:
                    freq[pattern] += 1
        return freq

    def frequency_words(self, text, k):
        """Calculates the most common combinations of adjacent nucleotides and adds them to a list.


        Arguments:
            text, k

        Returns:
            words


        """
        words = []
        freq = self.frequency_map(text, k)
        m = max(freq.values())
        for key in freq:
            if freq[key] == m:
                words.append(key)
        return words

    def reverse(self, pattern):
        """Reverses the pattern of nucleotides.

        Arguments:
            pattern

        Returns:
            reversed pattern

        """
        return pattern[::-1]

    def complement(self, pattern):
        complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        return ''.join(complement[base] for base in pattern)

    def reverse_complement(self, pattern):
        self.reverse(pattern)
        self.complement(pattern)
        return pattern

    def pattern_matching(self, pattern, genome):
        positions = []
        for i in range(len(genome) - len(pattern) + 1):
            if genome[i: i + len(pattern)] == pattern:
                positions.append(i)
        return positions
