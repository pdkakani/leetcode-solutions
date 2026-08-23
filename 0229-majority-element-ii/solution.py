class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        k = 3
        for num in nums:
            # if the candidate is already being tracked, increase its vote
            if num in counts:
                counts[num] += 1
            # if there is a room for a new candidate to be tracked    
            elif len(counts) < k - 1:
                counts[num] = 1
            else:
                # counts is full and the num is not what we are tracking, so this will reduce one vote from each candidates
                dead = []
                for c in counts:
                    counts[c] -= 1
                    if counts[c] == 0:
                        dead.append(c)
                # if the candidate gets down to ero votes, remove him from the race
                for c in dead:
                    del counts[c]
            
        # second pass to verify if thier actual votes exceeds the majority requirement n/k
        threshold = len(nums) // k

        # resetting the chosen candidates counts
        actual_count = defaultdict(int)
        for num in nums:
            if num in counts:
                actual_count[num] += 1
        
        result = []
        for candi in actual_count:
            if actual_count[candi] > threshold:
                result.append(candi)
        return result

            

        
