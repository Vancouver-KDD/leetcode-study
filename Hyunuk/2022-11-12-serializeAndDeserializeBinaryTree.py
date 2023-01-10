# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = collections.deque()
        ret = []
        if root:
            q.append(root)
        while q:
            node = q.popleft()
            if not node:
                ret.append("#")
                continue
            ret.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return ','.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(",")
        root = TreeNode(int(data[0]))
        i = 1
        q = collections.deque()
        q.append(root)
        while q and i < len(data):
            node = q.popleft()
            if data[i] != "#":
                left = TreeNode(int(data[i]))
                node.left = left
                q.append(left)
            i += 1
            if data[i] != "#":
                right = TreeNode(int(data[i]))
                node.right = right
                q.append(right)
            i += 1
            
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
