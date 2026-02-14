class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            # strings are immutable so you cant sort them like list using s.sort()
            key = "".join(sorted(s))
            ans[key].append(s)
        
        return list(ans.values())



