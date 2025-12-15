class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        old_to_new = {node: Node(node.val)}
        q = deque([node])

        while q:
            cur = q.popleft()

            for nei in cur.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)
                    q.append(nei)

                old_to_new[cur].neighbors.append(old_to_new[nei])

        return old_to_new[node]