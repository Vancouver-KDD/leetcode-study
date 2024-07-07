

# serialize it to a string

# deserialize it back to its original structure.


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
      # 1 2 N N 3 4 N N 5 N N
        res = []

        def inorderDFS(self, node):
            if not node:
                return
            res.append(str(node.val))
            inorderDFS(node.left)
            inorderDFS(node.right)
        inorderDFS(root)
        return ", ".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data.split(", ")

        # data = ["1", "2", "N", "N", "3", "4", "N", "N", "5", "N", "N"]

        def buildTree(self, data):
            if not data:
                return None
            val = data.pop(0)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = buildTree(data)
            node.right = buildTree(data)


# or

        # self.i = 0

        # data = data.split(',')
        # def buildTree(data):
        #     if not data:
        #         return None
        #     if data[self.i] == 'N':
        #         self.i += 1
        #         return None
        #     val = int(data[self.i])
        #     node = TreeNode(val)
        #     self.i += 1

        #     node.left = buildTree(data)
        #     node.right = buildTree(data)
        #     return node

        # return buildTree(data)
