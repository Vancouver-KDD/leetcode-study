class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = list(Counter(tasks).values())
        f_max = max(freq)
        max_count = freq.count(f_max)

        gaps_between_count = f_max - 1
        gap_part_include_current_char = n + 1
        empty_slots = gaps_between_count * gap_part_include_current_char + max_count

        return max(len(tasks), empty_slots)
        