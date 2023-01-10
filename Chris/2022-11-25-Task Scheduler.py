class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Keep track of the frequency of each task
        # The name of the tasks are not necesarry(only frequency matters)
        # Use max-heap to track the most frequent task
        # Idea: A greedy way. Always perform the most frequent task that is currently available. 
        
        # Use max heap to store currently available tasks as their frequency
        # Since we don't need to tell the name of tasks, we can just handle with their frequencies
        
        # To handle unavailable tasks in order, use queue and store tasks with their frequency and
        # next available time
        # Tasks that become unavailable first become available first as well
        # This is a FIFO type. => make use of queue
        
        
        # Count the frequency of each tasks and create a max heap
        counts = Counter(tasks)
        available = [-cnt for cnt in counts.values()]
        heapq.heapify(available)
        idle = collections.deque()
        time = 0
        # Increment time until there is no tasks left in the heap and q
        while available or idle:
            time += 1
            
            if available:
                # pop the most item from the heap, update frequency and put it in the queue
                # with next available time only if there is at least one task left
                task = heapq.heappop(available) + 1
                
                if task:
                    idle.append([task, time+n])
        
            # peek the first task in the queue and put it if the task is available
            if idle and idle[0][1]==time:
                heapq.heappush(available, idle.popleft()[0])
        # return the final time 
        return time
        