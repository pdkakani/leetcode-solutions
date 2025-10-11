class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        input_str = s.split(" ")
        input_pattern = list(pattern)
        if len(input_str) != len(input_pattern):
            return False
        return len(set(input_pattern)) == len(set(input_str)) == len(set(zip(input_pattern, input_str)))
        
