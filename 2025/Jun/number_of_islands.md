# 🏝️ Number of Islands: Study Notes

## 🎯 Core Idea

The strategy is to scan the entire grid. When we encounter a piece of land (`'1'`), we know we've found at least one part of an island. We then start a search (either DFS or BFS) from that point to find all connected land cells belonging to that *same* island. To avoid recounting, we "sink" the island by changing its cells from `'1'` to `'0'` (or another marker).

## ⚙️ Algorithm Breakdown

1.  Initialize an `island_count` to 0.
2.  Iterate through every cell of the grid using nested loops for `row` and `col`.
3.  At each cell `(row, col)`, check if its value is `'1'`.
    -   If it is, we have discovered a new, previously unvisited island.
    -   **Increment `island_count` by 1.**
    -   Call a search function (e.g., `dfs(grid, row, col)`) to find and "sink" all parts of this newly discovered island.
4.  After the loops complete, return `island_count`.

### The Search Function (DFS/BFS)

The job of the search function is to explore from a starting land cell and mark all connected land cells as visited.

**For a recursive DFS:**
-   **Base Case:** If the current `(row, col)` is out of bounds or the cell is not `'1'`, simply `return`.
-   **Action:** Change the current cell `grid[row][col]` from `'1'` to `'0'` to mark it as visited.
-   **Recurse:** Call the DFS function for all four neighbors (top, bottom, left, right).

---

## 🤔 Key Question: When to Increment the Count?

This is a crucial point of confusion.

-   **Incorrect:** Incrementing the count *inside* the DFS or BFS traversal. This would cause you to count every single piece of land instead of every island.
-   **Correct:** Increment the count in the main loop *only when you find a `'1'`*.

Think of it this way:
-   The **main loop** is the "discoverer."
-   The **DFS/BFS function** is the "explorer."

The discoverer finds a new, uncharted continent and raises a flag (increments `island_count`). The explorer then maps out and clears the entire continent (sinks the island) so the discoverer won't find and count it again.

---

## 📈 Complexity Analysis

Let `M` be the number of rows and `N` be the number of columns.

### Time Complexity: O(M * N)
-   The main nested loops visit every cell in the grid once.
-   The DFS/BFS function also visits each land cell at most once. Since we change `'1'` to `'0'`, we never process the same land cell twice.
-   Therefore, every cell is touched a constant number of times.

### Space Complexity: O(M * N)
-   This is dominated by the space required for the search traversal.
-   **DFS (Recursive):** In the worst-case scenario (a grid completely filled with land), the recursion depth can go up to `M * N`. This means the call stack could potentially hold all `M * N` cells.
-   **BFS (Iterative with a Queue):** The space complexity depends on the maximum size of the queue. In the worst case (a checkerboard or maze-like pattern), the queue could also hold a significant portion of the cells, up to O(M * N).

Both DFS and BFS have the same time and worst-case space complexity, so either approach is perfectly valid for this problem.