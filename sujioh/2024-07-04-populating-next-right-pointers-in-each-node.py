class Solution:
    def connect(self, root: 'curr_node') -> 'curr_node':
        if not root:
            return None
        
        queue = collections.deque([root])
        
        # start the traversal
        while queue:
            level_len = len(queue) # get number of nodes on the current level
            for i in range(level_len):
                curr_node = queue.popleft() 

                if i != level_len-1:
                    curr_node.next = queue[0]
                # the most left node each level has None as its next value
                else:
                    curr_node.next = None
                    
                if curr_node.left:
                    queue.append(curr_node.left) 
                if curr_node.right:
                    queue.append(curr_node.right)           
                
        return root