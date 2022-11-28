class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        Most_freq = freq.most_common()[0][1]
        Found_most = sum([freq[key] == Most_freq for key in freq])
        return max(len(tasks), (Most_freq - 1) * (n + 1) + Found_most)