# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, max_val):
            if not node:
                return
            if node.val >= max_val:
                self.count += 1
            max_val = max(node.val, max_val)
            dfs(node.left, max_val)
            dfs(node.right, max_val)
            ``
        dfs(root, float("-inf"))



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:

        
class Solution(object):
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, largerThan))
               
               
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        stack = collections.deque([])
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build_tree(preorder, inorder):
            if len(preorder) == 0 and len(inorder) == 0:
                return
            inorder_head_index = inorder.index(preorder[0])
            head = TreeNode(preorder[0])
            head.left = build_tree(preorder[1:inorder_head_index+1], inorder[:inorder_head_index])
            head.right = build_tree(preorder[inorder_head_index+1:], inorder[inorder_head_index+1:])
            return head
        return build_tree(preorder, inorder)
    
class WordNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = WordNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.child:
                node.child[i] = WordNode()
            node = node.child[i]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i not in node.child:
                return False
            node = node.child[i]
        if not node.end:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if i not in node.child:
                return False
            node = node.child[i]
        return True
    
class WordNode:
    
    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.child:
                node.child[i] = WordNode()
            node = node.child[i]
        node.end = True

    def search(self, word: str) -> bool:
        
        def wordSearch(root: WordNode, word: str) -> bool:
            node = root
            for idx, ch in enumerate(word):
                if ch == '.':
                    for child_node in node.child.values():
                        if wordSearch(child_node, word[idx+1:]):
                            return True
                    return False
                else:
                    if ch not in node.child:
                        return False
                    node = node.child[ch]
            return node.end
        return wordSearch(self.root, word)
    
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]
    
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])
    
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            pts.append([dist, x, y])

        res = []
        
        # heapd.heapify on list of list uses the first element in the child list
        heapq.heapify(pts)
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])
        return res
    
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]