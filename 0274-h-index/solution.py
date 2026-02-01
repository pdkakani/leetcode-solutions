class Solution:
    def hIndex(self, citations: List[int]) -> int:

        # n = len(citations)
        # h = 0
        # for i in range(n, 0, -1):
        #     count = 0
        #     j = 0
        #     while j < n:

        #         if citations[j] >= i:
        #             count += 1

        #             if count >= i:
        #                 h = i
        #                 return h

        #         j += 1
            
        # return h
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1: # At least (i+1) papers with >= (i+1) citations
                h = i + 1
        return h     
