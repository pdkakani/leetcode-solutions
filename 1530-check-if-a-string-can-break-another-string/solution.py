class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)

        # check if s1 can break s2
        can1 = all(s1[i] >= s2[i] for i in range(len(s1)))
        # check if s2 can break s1
        can2 = all(s2[i] >= s1[i] for i in range(len(s2)))

        return can1 or can2
