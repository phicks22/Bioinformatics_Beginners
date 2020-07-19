class Reader:

    def __init__(self, pattern):
        self.pattern = pattern

    def pattern_count(self, pattern, genome):
        count = 0
        n = len(genome)
        k = len(pattern)
        for i in range(n-k+1):
            if genome[i: i+k] == pattern:
                count += 1
        return count

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
                if text[j: j+k] == pattern:
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
        """Replaces the bases in the given pattern with the complementary base pairs.


        Arguments:
            pattern

        Returns:
            complementary strand


        """
        complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        return ''.join(complement[base] for base in pattern)

    def reverse_complement(self, pattern):
        """Utilizes the complement and reverse functions to return the reverse complement of the pattern.


        Arguments:
            pattern

        Returns:
            reverse complement


        """
        self.reverse(pattern)
        self.complement(pattern)
        return pattern

    def pattern_matching(self, pattern, genome):
        """Identifies the indices in which a given pattern can be found within a genome.


        Arguments:
            pattern, genome

        Returns:
            positions list

        """
        positions = []
        for i in range(len(genome) - len(pattern) + 1):
            if genome[i: i + len(pattern)] == pattern:
                positions.append(i)
        return positions

    def symbol_dict(self, genome, symbol):
        dict = {}
        n = len(genome)
        extended_genome = genome + genome[:n//2]
        dict[0] = self.pattern_count(symbol, genome[0:n//2])
        for i in range(1, n):
            dict[i] = dict[i-1]
            if extended_genome[i-1] == symbol:
                dict[i] = dict[i] - 1
            if extended_genome[i+(n//2)-1] == symbol:
                dict[i] = dict[i] + 1
        return dict


ex_1 = Reader('TGT')
print(ex_1.symbol_dict('TGTGCAGTACGTGTGCA', 'T'))
