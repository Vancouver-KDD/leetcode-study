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

    def exist(self, board, word: str) -> bool:
        def backtrack(row, col, visited, i):
            if i == len(word):
                return True
            if row < 0 or col < 0 or row >= m or col >= n or visited[row][col] or board[row][col] != word[i]:
                return False
            visited[row][col] = True
            if backtrack(row+1, col, visited, i+1) or backtrack(row-1, col, visited, i+1) or backtrack(row, col+1, visited, i+1) or backtrack(row, col-1, visited, i+1):
                return True
            visited[row][col] = False
            return False

        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if backtrack(row, col, visited, 0):
                    return True
        return False


def main():
    s = Solution()


if __name__ == "__main__":
    main()
