# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # initialize queue for BFS
        q = deque([root] if root else []);
        result = []
        
        # Start BFS search 
        while q:
            # iterate through each level
            level = []
            for _ in range(len(q)):
                currentNode = q.popleft()
                level.append(currentNode.val)
                if currentNode.left:
                    q.append(currentNode.left) 
                if currentNode.right:
                    q.append(currentNode.right)
            level.reverse() if len(result) % 2 else level
            result.append(level)
        return result
        
        
        # We want to take every single level 
        # And put it them into an array
        # And add that array into a final array
        # One problem is that each array at an odd index is going to be reversed. 
        # How can we traverse, BFS vs DFS
        # Both are okay but BFS is better since it is usually not recursive. DFS uses recursion to travel this tree. 
        
        # So, How do we do this zigzag where sometimes we are going to go in reverse direction.
        # Shold we jsut keep track of what level we are at and then traverse through that level in reverse? 
        # why not just go through each level from left to right but when it comes time to take this that array and then add it to a fianl array when this time comes, why not just take every odd level and then reverse this. lke change it to 20 and 9 and then add it to the result array.
        # for this, we are visiting every node twice but that does not change the overall time complexity magnitude. 
        # the space complexity is going to be Big O of n, BFS usually is an algorithm that tkaes a queue data structure. 
        