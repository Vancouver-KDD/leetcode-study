class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

'''
이 문에서 가장 중요한 것은 recursion 개념을 이해하는 것.
실제 isSameTree 메쏘드에서 recursion 부분을 제외하면, 엄청 간단함.

recursion 이해를 위해서 다음과 같은 예제와 콜스택을 준비함. 
아래 보이듯이 트리는 두 개이며, identical하다. 
콜스택을 프린트 할 때 쓴 코드는 아래 참조. 


    Tree 1                   Tree 2
      1                         1
     / \                       / \
    2   3                     2   3
   / \ / \                   / \ / \
  4  5 6  7                 4  5 6  7

Comparing Nodes: p.val=1, q.val=1
Comparing Nodes: p.val=2, q.val=2
Comparing Nodes: p.val=4, q.val=4
Comparing Nodes: p.val=5, q.val=5
Comparing Nodes: p.val=3, q.val=3
Comparing Nodes: p.val=6, q.val=6
Comparing Nodes: p.val=7, q.val=7

이 문제에서 내가 모르는 점은, 
recursion이 쓰인 경우, 콜스택 order를 모른다는 것이다.


----------------------------------------------------
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            # Base cases
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        # Recursive calls
        print(f"Comparing Nodes: p.val={p.val}, q.val={q.val}")
        left_result = self.isSameTree(p.left, q.left)
        right_result = self.isSameTree(p.right, q.right)
        
        return left_result and right_result
'''