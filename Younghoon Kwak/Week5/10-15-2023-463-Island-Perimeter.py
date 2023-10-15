class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        ans = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    ans += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        ans -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        ans -= 2
        return ans

 