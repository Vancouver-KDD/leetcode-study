# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] #result list
        q = deque([root]) #queue data structure for BFS and input root in there
        #q.append(root)

        while q: #while queue list is not empty, 
            qLen = len(q) #get the len of q since we will go through these and put them in a list
            level = [] #temporary list before putting our list into the result list
            for i in range(qLen): #iterate over all the items in our queue
                node = q.popleft() #pop the left value (since queue, pop from left and add to the riight)
                if node: #if node exists:
                    level.append(node.val) #append node (value since node will igve you a tree) onto the level
                    q.append(node.left) #append left node of the node to the queue
                    q.append(node.right) #append right nbode of the node to the queue
            if level: #if level is not null, append it onto the result
                res.append(level)
        return res

        #time complexity is O(n) since we will visit every node
        # space complexity is O(n) since our queue could have up to 