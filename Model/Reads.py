def frequency_map(text, k):
    freq = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i: i+k]
        freq[pattern] = 0
        for j in range(n-k+1):
            if freq[pattern] == pattern:
                freq[pattern] += 1
    return freq

