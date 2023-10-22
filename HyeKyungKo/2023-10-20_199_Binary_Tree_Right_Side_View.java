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

//limitation : Is it full binary tree?? No.

//Idea: bfs search using queue

//Time Complexity: O(N)
//Space Complexity: O(N), 좀더 자세히는 O(D), D is a tree diameter. Worst case is D = N/2 => O(N)

class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        
        if(root == null){
            return result;
        }
        
        Queue<TreeNode> bfs = new LinkedList<>();
        
        bfs.add(root);
        
        while(!bfs.isEmpty()){
            int size = bfs.size();
            
            TreeNode leave = null;
            for(int i = 0; i < size; i++){
                leave = bfs.remove();
                if(leave.left != null){
                    bfs.add(leave.left);
                }
                if(leave.right != null){
                    bfs.add(leave.right);
                }
            }
            if(leave != null){
                result.add(leave.val);
            }
        }
        
        return result;
    }
}


//idea2: DFS  (leetcode solution 에 BFS 와 DFS 둘다 있음. 나는 BFS 로 했고, DFS 는 솔루션을 보고 만듬. )
//Time Complexity: O(N)
//Space Complexity: O(N), 좀더 자세히는 O(H), H is tree height. 그러나 역시 Worst case 의 경우 H = N 임 
/*
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if(root == null){
            return result;
        }
        
        dfs(root, 0, result);
        return result;
    }
    
    //[1,2,3,null,5,null,4]
    //root: 1,
    //level:0,  
    //result:[]->[1]->[1,3]->[1,3,4]
    void dfs(TreeNode root, int level, List<Integer> result){
        
        if(root == null){
            return;
        }
        
        if(level == result.size()){
            result.add(root.val);
        }
        
        dfs(root.right, level+1, result);
        dfs(root.left, level+1, result);
    }
}
*/