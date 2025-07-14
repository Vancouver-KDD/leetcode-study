## 102. Binary Tree Level Order Traversal

```
class Solution102 {
    public List<List<Integer>> levelOrder(TreeNode root) {
        // 1. 결과를 담을 리스트
        List<List<Integer>> result = new ArrayList<>();
        // 2. 뿌리가 없으면 빈 리스트 반환
        if (root == null) {
            return result;
        }
        // 3. BFS를 위해 큐에 뿌리 넣기
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        // 4. 큐가 빌 때까지 반복
        while (!queue.isEmpty()) {
            // 4-1. 현재 레벨 크기(노드 수) 저장
            int levelSize = queue.size();
            List<Integer> level = new ArrayList<>();

            // 4-2. 이 레벨에 속한 모든 노드를 처리
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                // 4-3. 값 추가
                level.add(node.val);
                // 4-4. 자식이 있으면 다음 레벨 큐에 추가
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            // 4-5. 한 레벨이 끝나면 결과에 추가
            result.add(level);
        }

        // 5. 모든 레벨을 담은 리스트 반환
        return result;
    }
}

```
