# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        if not root:
            return ''
        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if not node:
                result.append('N')
                result.append(',')
                continue

            result.append(str(node.val))
            result.append(',')
            queue.append(node.left)
            queue.append(node.right)

        return "".join(result[0:len(result) - 1])

    def deserialize(self, data):
        if data == '':
            return None

        data = data.split(",")[::-1]
        queue = deque()

        root = TreeNode(data.pop())
        queue.append(root)

        while data:
            curr_node = queue.popleft()

            left_child = data.pop()
            if left_child != 'N':
                left = TreeNode(int(left_child))
                curr_node.left = left
                queue.append(left)

            right_child = data.pop()
            if right_child != 'N':
                right = TreeNode(int(right_child))
                curr_node.right = right
                queue.append(right)

        return root

    def serializeDFS(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def dfs(root):
            if not root:
                path.append("N")
                path.append(",")
                return

            path.append(str(root.val))
            path.append(",")
            dfs(root.left)
            dfs(root.right)

        path = []
        dfs(root)
        return "".join(path[0:len(path) - 1])

    def deserializeDFS(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs(node):
            if len(arr) == 0:
                return None

            curr_value = arr.pop()

            if curr_value == 'N':
                return None

            node = TreeNode(int(curr_value))
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            return node

        arr = data.split(',')[::-1]
        return dfs(None)