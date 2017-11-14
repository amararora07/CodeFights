def almostIncreasingSequence(sequence):
    for i, x in enumerate(sequence):    
        s = sequence[:i]
        s.extend(sequence[i+1:])
        if s == sorted(set(s)):
            return True
    return False
