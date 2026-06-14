class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # best server to use (weight,  index)
        free = [(w,i) for i, w in enumerate(servers)]
        heapq.heapify(free)

        busy = []
        ans = []
        time = 0


        for j in range(len(tasks)):
            time = max(time, j) # this is to make sure we jump to the time where the next task arrives, task's arrival time

            if not free:
                time= busy[0][0] # jump to clock when next server frees up, server's free time

            while busy and busy[0][0] <= time:
                ft, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w,i))
            
            w, i = heapq.heappop(free)
            ans.append(i)
            heapq.heappush(busy, (time + tasks[j], w, i))

        return ans
        
