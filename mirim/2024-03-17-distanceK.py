# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        if k == 0:
            res = [target.val]
            return res

        graph = collections.defaultdict(list)
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                q.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                q.append(node.right)

        visited = set([target])
        q = collections.deque([target])
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if level == k:
                    res.append(node.val)
                else:
                    for edge in graph[node]:
                        if edge not in visited:
                            visited.add(edge)
                            q.append(edge)
            level += 1
        return res
