/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 //2022-11-29 --iteration: leetcode 의 해법으로 풀이 ( binary search tree 는 값이 정렬되어있음. )
 //Time Complexity : O(N) <-- 모든 node 가 left 만 있거나 right 만 있으면 최대 방문수가 N개
 //Space Complexity: O(1) 
class Solution{
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q){
        if(root == null || p == null || q == null){
            return null;
        }

        TreeNode node = root;
        while(node != null){
            if(p.val < node.val && q.val < node.val){
                node = node.left;
            }else if(p.val > node.val && q.val > node.val){
                node = node.right;
            }else{// one of value is root.val , or one of value is in left tree, the other value is in right tree
                return node;
            }
        }

        return null;
    }
}

 //2022-11-29 --recusrive: leetcode 의 해법으로 풀이 ( binary search tree 는 값이 정렬되어있음. )
 //Time Complexity : O(N) <-- 모든 node 가 left 만 있거나 right 만 있으면 최대 방문수가 N개
 //Space Complexity: O(N) <-- 모든 node 가 left 만 있거나 right 만 있으면 최대 stack depth 가 N  
 /*
class Solution{
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q){
        if(root == null || p == null || q == null){
            return null;
        }

        if(p.val < root.val && q.val < root.val){
            return lowestCommonAncestor(root.left, p, q);
        }else if(p.val > root.val && q.val > root.val){
            return lowestCommonAncestor(root.right, p, q);
        }else{ // one of value is root.val , or one of value is in left tree, the other value is in right tree
            return root;
        }
    }
}
*/

//2022-11-29
//나는 트리의 값들이 정렬 (left tree value < root < right tree value)되어있다고 생각을 안하고 아래처럼 풀었음  
//Time Complexity :O(N)
//Space Complexity: O(N)  //recursive
/*
class Solution {
    boolean successFind; 
    TreeNode ancestor;
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null || p == null || q == null){
            return null;
        }
        ancestor = null;
        successFind = false;
        findValue(root, p, q);

        return ancestor;
    }

    private boolean findValue(TreeNode root, TreeNode p, TreeNode q){

        if(root == null || successFind){ //if root is null, or if finding 2 values are already done, we don't need to search any more.
            return false;
        }

        boolean existLeft = findValue(root.left, p, q);
        boolean existRight = findValue(root.right, p, q);

        if(existLeft && existRight){
            successFind = true;
            ancestor = root;
            return true;
        }else if(existLeft || existRight){
            if(root.val == p.val || root.val == q.val){
                successFind = true;
                ancestor = root;
            }
            return true;
        }
        if(root.val == p.val || root.val == q.val){
            return true;
        }
        return false;
    }
}
*/