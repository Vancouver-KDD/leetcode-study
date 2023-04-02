"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed)
 of all the values of the nodes in the tree.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # Create an adjacency list to store the course dependencies
        graph = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        # Create a list to store the state of each course
        state = [0 for _ in range(numCourses)]

        def dfs(course):
            # Mark the current course as being visited
            state[course] = 1
            for neighbor in graph[course]:
                if state[neighbor] == 1:
                    # A cycle is detected, return false
                    return False
                if state[neighbor] == 0:
                    if not dfs(neighbor):
                        return False
            state[course] = 2
            return True

        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return False
        # If all courses can be finished, return true
        return True


def main():
    s = Solution()


if __name__ == "__main__":
    main()
