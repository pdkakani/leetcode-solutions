class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        i = Counter(s)
        j = Counter(t)

        return i == j
