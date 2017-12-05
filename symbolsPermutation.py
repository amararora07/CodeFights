def symbolsPermutation(word1, word2):
        l=list(word1)
        s=list(word2)
        l.sort()
        s.sort()
        return l==s
