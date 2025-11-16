class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n = len(operations)
        scores = deque()
        summ = 0

        for i in range(n):
            if operations[i] != "C" and operations[i] != "D" and operations[i] != "+":
                scores.append(operations[i])
            elif operations[i] == "C":
                scores.pop()
            elif operations[i] == "D":
                scores.append(int(scores[-1]) * 2)
            elif operations[i] == "+":
                scores.append(int(scores[-1]) + int(scores[-2]))
        
        return sum(int(s) for s in scores)

