class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []
        cooldown = deque()
        res = 0
        for f in freq.values():
            heappush(heap, -f)

        while heap or cooldown:
            if heap:
                task = -heappop(heap)
                if task > 1:
                    cooldown.append((task - 1, res + n + 1))
            res += 1

            while cooldown and cooldown[0][1] == res:
                task_c, freq_c = cooldown[0]
                cooldown.popleft()
                heappush(heap, -task_c)
        return res
