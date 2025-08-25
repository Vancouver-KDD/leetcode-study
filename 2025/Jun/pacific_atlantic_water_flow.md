# 🌊 Pacific Atlantic Water Flow: Study Notes

## 🧠 Initial Brain Dump & Algorithm Idea

This is the raw thought process for solving the problem:

-   The core idea is to use Depth First Search (DFS).
-   The DFS function signature would look something like: `dfs(ocean_set, row, col, prev_height)`.
-   **Base Case:** The search stops if the current cell `(row, col)` is out of bounds or has already been visited for the current ocean.
-   **Recursive Step:** Water can flow "inland" from a cell to a neighbor if the neighbor's height is greater than or equal to the current cell's height (`heights[neighbor] >= prev_height`).
-   If the condition is met, mark the cell as visited by adding it to the respective ocean's set (`pacific` or `atlantic`) and recursively call DFS for its neighbors.
-   Start the DFS from all the border cells:
    -   Top and bottom rows.
    -   Left and right columns.
-   The final answer is the set of coordinates that are present in *both* the `pacific` and `atlantic` sets.

---

## ⚠️ Common Pitfalls & Corrections

Here are some common mistakes made during implementation, based on initial attempts.

### 1. Out of Bounds Check
**Mistake:** `if row > row_len or col > col_len`
**Correction:** This is incorrect. Array indices go from `0` to `len - 1`. The check must be for `>=` and also for negative indices. A correct check is: `if not (0 <= row < row_len and 0 <= col < col_len)`.

### 2. Visited Marking
**Mistake:** Modifying the input grid to mark visited cells, for example, `heights[row][col] = 0`.
**Correction:** Use a separate `set` or a boolean matrix for visited tracking for each ocean.

> **Q: Why not destroy the original matrix? It's a one-time use, right?**
> **A:** You need to run the search process twice: once for the Pacific ocean and once for the Atlantic. If you zero-out cell heights during the Pacific DFS, that height information is lost. When you then run the Atlantic DFS, the height comparisons (`prev_height <= heights[r][c]`) will be incorrect, leading to the wrong result.

### 3. Storing Ocean Cells
**Mistake:** Using a `list` to store reachable cells and then trying to check for intersection with `if pacific[i] and atlantic[j]`.
**Correction:** Use a `set` to store the `(row, col)` tuples. Sets provide a highly efficient `O(1)` average time complexity for checking membership (`(r, c) in my_set`) and a simple operator `&` for finding the intersection.

### 4. Border DFS Calls
**Mistake:** Calling DFS with an index equal to the length, like `dfs(atlantic, i, col_len, ...)`.
**Correction:** The last valid index is `len - 1`. Ensure the calls use the correct indices, e.g., `dfs(atlantic, i, col_len - 1, ...)`.

### 5. Final Loop for Results
**Mistake:** Incorrectly checking for membership, e.g., `if pacific[i]`.
**Correction:** Iterate through the intersection of the two sets. For a coordinate `(r, c)`, the check is `if (r, c) in pacific and (r, c) in atlantic`.

---

## 🐍 Code Deep Dive: Pythonic Intersection

A very clean way to get the final result in Python involves set intersection and list comprehension.

### The Python Code
```python
# Assuming 'pacific' and 'atlantic' are sets of (row, col) tuples
res = [[r, c] for (r, c) in pacific & atlantic]
```

### How It Works
1.  **`pacific & atlantic`**: This is the set intersection operator in Python. It creates a *new set* containing only the coordinates that are present in **both** the `pacific` and `atlantic` sets. For example, if `pacific = {(0,1), (0,2)}` and `atlantic = {(0,2), (1,2)}`, the intersection is `{(0,2)}`.

2.  **`for (r, c) in ...`**: This loop iterates through each coordinate tuple `(r, c)` in the newly created intersection set.

3.  **`[[r, c] ... ]`**: This is a **list comprehension**. It's a concise way to build a list. For each tuple `(r, c)` from the loop, it creates a list `[r, c]` and adds it to the final result list, `res`. This is done to match the problem's required output format of a list of lists (`[[row, col], ...]`).

### JavaScript Equivalent for Understanding
To better understand what the Python one-liner does, here is the equivalent logic written in JavaScript. This version is more verbose but shows the step-by-step process clearly.

```javascript
// Assuming 'pacific' and 'atlantic' are Sets of string coordinates like "row,col"
const res = [];

for (let coord of pacific) {
  // Check if the coordinate from pacific also exists in atlantic
  if (atlantic.has(coord)) {
    // If it exists in both, parse it back into numbers and add to result
    const [r, c] = coord.split(",").map(Number);
    res.push([r, c]);
  }
}

// 'res' now holds the final list of [row, col] pairs.
// This is the long form of what the Python list comprehension achieves.
```