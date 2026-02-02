class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_tank = 0
        current_tank = 0
        start = 0

        for i in range(n):
            net_gain = gas[i] - cost[i]
            total_tank += net_gain
            current_tank += net_gain

            if current_tank < 0:
                start = i + 1
                current_tank = 0
        return start if total_tank >= 0 else -1
