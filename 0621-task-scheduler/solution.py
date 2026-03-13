class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown = deque() # (remaining_freq_negated, avai_at_time)
        freq = Counter(tasks)
        heap = [-f for f in freq.values()]
        heapify(heap)

        time = 0

        while heap or cooldown:
            time += 1

            #release fron cooldown if read
            while cooldown and cooldown[0][1] <= time:
                heappush(heap, cooldown.popleft()[0])
            
            if heap:
                #pick most frequent task
                remaining = heappop(heap) + 1 #+1 because freq are negated
                if remaining < 0: #still has runs left
                    cooldown.append((remaining, time + n+1))
            else:
                #nothing available
                #jump time to when next available
                time = cooldown[0][1] - 1
        
        return time
            


            

        
        
        
