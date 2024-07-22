class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # left top: pacific, right bottom: atlantic
        # Create two 2D lists name pacific/Altantic
        # recursion -> check Pacific/Altlantic -> if it can go set True, otherwise False
        if not heights or not heights[0]:
            return []

        pacific_q = deque()  # left top
        atlantic_q = deque()  # right bottom

        for i in range(len(heights)):
            pacific_q.append((i, 0))
            atlantic_q.append((i, len(heights[0]) - 1))
        for i in range(len(heights[0])):
            pacific_q.append((0, i))
            atlantic_q.append((len(heights) - 1, i))

        def check_reachable(queue):
            reachable = set()
            while queue:
                (row, col) = queue.popleft()
                reachable.add([row, col])
                for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_row, new_col = row + x, col + y
                    if new_row < 0 or new_row >= len(heights) or new_col < 0 or new_col >= len(heights[0]):
                        continue
                    if (new_row, new_col) in reachable:
                        continue
                    if heights[new_row][new_col] < heights[row][col]:
                        continue

                    queue.append((new_row, new_col))
            return reachable

            pacific_reachable = check_reachable(pacific_q)
            atlantic_reachable = check_reachable(atlantic_q)

            return list(pacific_reachable.intersection(atlantic_reachable))