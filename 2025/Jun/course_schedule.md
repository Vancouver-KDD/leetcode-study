# 🎓 Course Schedule: Detecting Cycles in a Graph

## 🎯 Core Idea

The problem "can you finish all courses?" is a classic graph problem in disguise. It's equivalent to asking: **"Is there a cycle in the directed graph representing course prerequisites?"**

-   Each course is a **node**.
-   Each prerequisite relationship `[course, prereq]` is a **directed edge** from `prereq` to `course`.

If there is a cycle (e.g., Course A needs B, and B needs A), it's impossible to finish. We can detect this using Depth First Search (DFS).

---

## ⚙️ Algorithm: 3-State DFS

To safely detect a cycle, we need to track the state of each node during the traversal.

1.  **Build the Graph:** Create an adjacency list (e.g., a hash map) where `graph[course]` contains a list of prerequisites for that course.
2.  **Initialize States:** Create a `states` array to track the status of each course. We use three states:
    -   `0`: **Unvisited**. The default state; we haven't processed this node yet.
    -   `1`: **Visiting**. We are currently exploring this node's path in the current DFS traversal. This is the key to detecting a cycle.
    -   `2`: **Visited**. We have fully explored this node and all its descendants and found no cycles.
3.  **Run DFS:** Iterate through each course from `0` to `numCourses - 1`. If a course is `unvisited`, start a DFS from it.

### DFS Logic
-   If a node is `visiting` (`state == 1`), we've looped back on our current path. **A cycle is detected**, so return `False`.
-   If a node is `visited` (`state == 2`), we've already confirmed this path is safe. We can return `True` immediately.
-   Mark the current node as `visiting` (`state = 1`).
-   Recursively call DFS on all its prerequisites. If any call returns `False`, propagate it up.
-   If all prerequisite paths are safe, mark the current node as `visited` (`state = 2`) and return `True`.

---

## 🤔 Deep Dive: Why 3 States are Essential

A common question is, "Why not just use two states: `unvisited` and `visited`?"

Using only two states cannot distinguish between a true cycle and a path that safely revisits an already-cleared node.

**Example Graph:** `0 -> 1`, `3 -> 1`, `1 -> 2`, `2 -> 4`, `4 -> 3` (Cycle: `1 -> 2 -> 4 -> 3 -> 1`)

**With only 2 states (unvisited, visited):**
1.  Start DFS from `0`. Mark `0` as `visited`.
2.  Explore `0`'s prerequisite (none). Path `0` is safe.
3.  Start DFS from `1`. Mark `1` as `visited`.
4.  Explore `1`'s prerequisite `2`. Mark `2` as `visited`.
5.  Explore `2`'s prerequisite `4`. Mark `4` as `visited`.
6.  Explore `4`'s prerequisite `3`. Mark `3` as `visited`.
7.  Explore `3`'s prerequisite `1`. **Problem:** Node `1` is already `visited`. A 2-state system would have to assume this is a cycle and return `False`, which is correct here.

**But consider a non-cycle graph:** `0 -> 1`, `2 -> 1`.
1.  Start DFS from `0`. Path is safe. Mark `0` as `visited`.
2.  Start DFS from `2`. Mark `2` as `visited`.
3.  Explore `2`'s prerequisite `1`. Mark `1` as `visited`.
4.  Explore `1`'s prerequisite `0`. **Problem:** Node `0` is `visited`. A 2-state system would incorrectly flag this as a cycle.

**The 3-state solution (`visiting`) solves this:**
-   A node marked `visiting` means it's in our **current recursion stack**. Hitting it again means we've looped back on ourselves—a true cycle.
-   A node marked `visited` means it was fully explored in a *previous* DFS call and confirmed to be safe. Hitting it again is fine; we don't need to re-explore it.

---

## 📈 Complexity Analysis

Let `N` be `numCourses` and `P` be the number of prerequisites (edges).

### Time Complexity: O(N + P)
-   **Building the graph:** We iterate through all `P` prerequisites once, which is O(P).
-   **DFS Traversal:** Each node and edge is visited at most once across all DFS calls. This is because once a node's state becomes `2` (visited), we never explore it again. The total cost is O(N + P).

### Space Complexity: O(N + P)
-   **Adjacency List:** Stores all `P` edges, so O(P).
-   **State Array:** Stores a state for each of the `N` courses, so O(N).
-   **Recursion Stack:** In the worst case (a long chain of prerequisites), the DFS recursion depth can be up to `N`, so O(N).