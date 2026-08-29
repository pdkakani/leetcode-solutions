class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fr_count = defaultdict(int)

        left = 0
        res = 0

        for right, fruit in enumerate(fruits):
            fr_count[fruit] += 1

            while len(fr_count) > 2:
                left_fruit = fruits[left]
                fr_count[left_fruit] -= 1
                if fr_count[left_fruit] == 0:
                    del fr_count[left_fruit]
                left += 1
            res = max(res, right - left + 1)
        return res 

        
