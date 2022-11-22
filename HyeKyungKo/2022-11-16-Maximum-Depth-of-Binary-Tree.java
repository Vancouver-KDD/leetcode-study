/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
 //2022-11-16
 //limitation:??
 //DFS
//Time Complexity: O(N) <-- 모든 노드 방문
//Space Complexity: O(트리높이) <-- node 가 left 로만 또는 right 로만 있으면 트리높이가 O(N), balanced tree  이면 이진트리이니까 트리높이는 O(logN)
/*
class Solution{
    public int maxDepth(TreeNode root){
        if(root == null){
            return 0;
        }

        int leftMaxDepth = maxDepth(root.left);
        int rightMaxDepth = maxDepth(root.right);

        int depth = Math.max(leftMaxDepth, rightMaxDepth);

        return depth+1;
    }
}
*/
//BFS
//Time Complexity:O(N) <-- 모든노트 탐색
//Space Complexity: O(the maximum number of nodes at the same level ) 
class Solution{
    public int maxDepth(TreeNode root){
        if(root == null){
            return 0;
        }

        Queue<TreeNode> queue = new LinkedList<TreeNode>(); 
        queue.add(root);
        int depth = 0;
        int nodeNum = 1; //the number of nodes at the same level
        while(!queue.isEmpty()){

            int count = 0;
            int currNum = 0;
            while(count < nodeNum){
                TreeNode node = queue.remove();
                if(node.left != null){
                    currNum++;
                    queue.add(node.left);
                }
                if(node.right != null){
                    currNum++;
                    queue.add(node.right);
                }
                count++;
            }
            nodeNum = currNum; //update the number of nodes
            depth++;
            
        }
        return depth;
    }
}


/*
class Solution {
    
    public int maxDepth(TreeNode root) {
        
        if(root == null){
            return 0;
        }

        Queue<Pair<TreeNode, Integer>> queue = new LinkedList();
        int maxDepth = 0;
        queue.add(new Pair(root, 1));
        
        while(!queue.isEmpty()){
            Pair<TreeNode, Integer> data = queue.poll();
            TreeNode node = data.getKey();
            int depth = data.getValue();
            
            maxDepth = Math.max(maxDepth, depth);
            if(node.left != null){
                queue.offer(new Pair(node.left, depth+1));
            }
            if(node.right != null){
                queue.offer(new Pair(node.right, depth+1));
            }
        }
        
        return maxDepth;
    }  
}
*/
    //2022.04.09 ----- my solution
    /*
    public int maxDepth(TreeNode root) {
        
        if(root == null){
            return 0;
        }

        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);
        
        int depth = Math.max(leftDepth, rightDepth);
        
        return depth+1;
    }
    */

