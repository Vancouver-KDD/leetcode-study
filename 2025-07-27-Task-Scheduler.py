class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = list(freq.values()).count(max_freq)
        
        part_count = max_freq - 1
        part_length = n + 1
        total_slots = part_count * part_length + max_count
        
        return max(len(tasks), total_slots)
