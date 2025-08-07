def leastInterval(tasks, n):
    count = [0] * 26
    for ch in tasks:
        count[ord(ch) - ord('A')] += 1

    max_freq = 0
    max_count = 0
    for c in count:
        if c > max_freq:
            max_freq = c
            max_count = 1
        elif c == max_freq:
            max_count += 1

    part_count = max_freq - 1
    part_len = n - (max_count - 1)
    empty_slots = part_count * part_len
    remaining_tasks = len(tasks) - max_freq * max_count
    idles = max(0, empty_slots - remaining_tasks)

    return len(tasks) + idles
