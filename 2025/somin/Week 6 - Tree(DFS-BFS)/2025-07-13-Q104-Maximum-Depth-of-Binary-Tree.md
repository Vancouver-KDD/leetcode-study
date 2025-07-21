## 104. Maximum Depth of Binary Tree

```
class Solution104 {
    public int maxDepth(TreeNode root) {
        // 1. 뿌리(root)가 없으면 높이는 0
        if (root == null) {
            return 0;
        }
        // 2. 왼쪽 서브트리의 높이를 재고
        int left = maxDepth(root.left);
        // 3. 오른쪽 서브트리의 높이를 재고
        int right = maxDepth(root.right);
        // 4. 두 값 중 큰 값에 +1 한 것이 현재 노드 높이
        return Math.max(left, right) + 1;
    }
}
```
