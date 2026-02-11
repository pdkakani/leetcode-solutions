class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        num_words = len(words)
        res = []
        word_len = len(words[0])
        
        word_counter = Counter(words)
        for start in range(word_len):
            left = start
            right = start
            current_counter = Counter()
            words_used = 0

            #slide window
            while right + word_len <= len(s):

                word = s[right:right + word_len]
                if word in word_counter:
                    current_counter[word] += 1
                    words_used += 1

                    #check for duplicates
                    while current_counter[word] > word_counter[word]:
                        left_word = s[left: left+word_len]
                        current_counter[left_word] -= 1
                        words_used -= 1
                        left += word_len
                    
                    #check if window is valid
                    if words_used == num_words:
                        res.append(left)
                else:
                    current_counter.clear()
                    words_used = 0
                    left = right + word_len
                right += word_len
        return res
                
