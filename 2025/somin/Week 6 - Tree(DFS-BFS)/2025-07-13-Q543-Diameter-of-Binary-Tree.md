## 543. Diameter of Binary Tree

```
class Solution543 {
    // 1. 전체 트리에서 가장 긴 경로를 저장할 변수
    private int maxDiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        // 2. 높이 계산 과정에서 maxDiameter를 함께 업데이트
        calculateHeight(root);
        // 3. 최종적으로 저장된 가장 긴 경로 길이를 반환
        return maxDiameter;
    }

    private int calculateHeight(TreeNode node) {
        // 4. 빈 노드면 높이는 0
        if (node == null) {
            return 0;
        }
        // 5. 왼쪽 서브트리 높이 계산
        int leftHeight = calculateHeight(node.left);
        // 6. 오른쪽 서브트리 높이 계산
        int rightHeight = calculateHeight(node.right);
        // 7. 이 노드를 지나는 경로 길이 = 왼쪽 높이 + 오른쪽 높이
        maxDiameter = Math.max(maxDiameter, leftHeight + rightHeight);
        // 8. 현재 노드의 높이 = 더 큰 자식 높이 +1
        return Math.max(leftHeight, rightHeight) + 1;
    }
}

```
