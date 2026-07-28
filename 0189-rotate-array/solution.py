class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # pointer method
        # imagine its numbers sitting on chair in a circle

        start = 0
        count = 0

        n = len(nums)

        while count < n:
            curr_idx = start
            prev_value = nums[start]

            while True:
                next_idx = (curr_idx + k) % n
                nums[next_idx], prev_value = prev_value, nums[next_idx]

                curr_idx = next_idx
                count += 1

                if start == curr_idx:
                    break

            start += 1
