class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        
        res = []
        word_len = len(words[0])
        num_words = len(words)
        word_count = Counter(words)

        for start in range(word_len):
            left = start
            right = start
            current_count = Counter()
            words_used = 0

            # slide window by word len
            while right + word_len <= len(s):
                #get the word at right pointer
                word = s[right: right + word_len]

                #if word is in our list
                if word in word_count:
                    current_count[word] += 1
                    words_used += 1

                    # if we have too many of this word, shrink from left
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        words_used -= 1
                        left += word_len
                    
                    #check if we have valid window
                    if words_used == num_words:
                        res.append(left)
                else:
                    #word not in list, reset window
                    current_count.clear()
                    words_used = 0
                    left = right + word_len
                right += word_len
        return res
                


        
