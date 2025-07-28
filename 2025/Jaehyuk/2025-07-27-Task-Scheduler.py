class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) #count each task element
        maxHeap = [-cnt for cnt in count.values()] #most frequent in order
        heapq.heapify(maxHeap) #order it in maxheap
        time = 0
        q = deque() #frequent, time + n so pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
        