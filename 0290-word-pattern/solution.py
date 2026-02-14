class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # words = s.split()
        # if len(pattern) != len(words):
        #     return False

        # pat = Counter(pattern)
        # words_counter = Counter(words)
        
        # if Counter(pat.values()) != Counter(words_counter.values()):
        #     return False
        
        # word_pat_map = dict(zip(pat, words_counter))

        # for i in range(len(pattern)):
        #     letter = pattern[i]
        #     word = word_pat_map[letter]
        #     if word != words[i]:
        #         return False
        # return True

        letters = list(pattern)
        words = s.split()

        if len(letters) != len(words):
            return False
        
        return len(set(letters)) == len(set(words)) == len(set(zip(letters,words)))
