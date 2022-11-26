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
//2022-11-25 Inorder traversal 이용 <-- min 값만 계속 비교하면됨
// ==>  left < root < right  를 recursive 하게 비교하게됨
//limitation: node value can have same value? . 
// value 의 min, max 값이 Integer 의 MIN, MAX 이기때문에 
// 시작 min 값을 null 로 설정하고 비교하도록 함. 
//Time Complexity: O(N)
//Space Complexity: O(N)

//Inorder traversal - iteration 방식
class Solution{
    public boolean isValidBST(TreeNode root){
        Stack<TreeNode> stack = new Stack<>();

        if(root == null){
            return true;
        }

        Integer min = null;
        TreeNode currNode = root;

        while(!stack.isEmpty() || currNode != null){
            
            if(currNode != null){
                stack.push(currNode);
                currNode = currNode.left;
            }else{
                currNode = stack.pop();
                //compare 
                if(min != null && currNode.val <= min){
                    return false;
                }
                min = currNode.val;
                currNode = currNode.right;

            }
        }

        return true;
    }
}

//Inorder traversal - recursive 방식
/*
class Solution{
    Integer min = null;
    public boolean isValidBST(TreeNode root){
        return inorderTraversal(root);
    }

    private boolean inorderTraversal(TreeNode root){
        if(root == null){
            return true;
        }

        if(!inorderTraversal(root.left)){
            return false;
        }

        if(min != null && root.val <= min){
            return false;
        }
        min = root.val;

        return inorderTraversal(root.right);
    }
    
}
*/
 //2022-11-25-Min/MAX를 이용한 DFS
//limitation: node value can have same value? 
//min, max 로 Integer.MIN_VALUE, Integer.MAX_VALUE 를 설정하면 아래 case 에서 error 가 생김
// Input : [2147483647] -> Output : true 이여야 하는데 false 가 나옴. 
// [2147483647] <-- 이 값이 Integer.MAX_VALUE 이기 때문. 
// 따라서 이런경우를 위해 양극단을 null 로 체크하도록 변경
//Time Complexity: O(N)
//Space Complexity: O(N)
/*
class Solution{
    public boolean isValidBST(TreeNode root){

        return recursiveCheckBST(root, null, null);

    }
    private boolean recursiveCheckBST(TreeNode root, Integer min, Integer max ){
        if(root == null){
            return true;
        }

        if((min != null && root.val <= min) || (max != null && root.val >= max)){
            return false;
        }

        return recursiveCheckBST(root.left, min, root.val) &&
                recursiveCheckBST(root.right, root.val, max);
    }
}
*/

//2022.09.18
// Limitation: if root is null, return false
// Input: root = [2,1,3] --> Output: true
// Input: root = [5,1,4,null,null,3,6] --> Output: false

//Approach#1 - Top-down DFS
// Time Complexity: O(n), Space Complexity: O(n)
/*
class Solution {
    public boolean isValidBST(TreeNode root) {
        
        if(root == null){
            return false;
        }
        
        // initial minVal is null, initial maxVal is null <--- treenode 가 가질수 있는 value 의 범위가 Integer.MIN_VALUE, Integer.MAX_VALUE 를 포함하기때문에 이렇게 null 값을 이용해 양극단을 체크 하도록 함. 
        return validateTree(root, null, null);
        
    }
    
    boolean validateTree(TreeNode root, Integer minVal, Integer maxVal){
        
        if(root == null){
            return true;
        }
        
        if((minVal != null && minVal >= root.val) || (maxVal != null) && root.val >= maxVal){
            return false;
        } 
        
        if(!validateTree(root.left, minVal, root.val)){
            return false;
        }
        
        if(!validateTree(root.right, root.val, maxVal)){
            return false;
        }
        
        return true;
    }
}
*/

//Approach#2 - Inorder Traversal (left -> root -> right)
//Time Complexity: O(n), Space Complexity: O(n)
/*
class Solution {
    
    Integer prevVal = null;
    
    public boolean isValidBST(TreeNode root) {
        
        if(root == null){
            return false;
        }
        
        return inorderTrav(root);
        
    }
    
    boolean inorderTrav(TreeNode root){
        if(root == null){
            return true;
        }
        
        if(!inorderTrav(root.left)){
            return false;
        }        
        
        if((prevVal != null ) && (root.val <= prevVal)){
            return false;
        }
        
        prevVal = root.val;
        
        if(!inorderTrav(root.right)){
            return false;
        }
        
        return true;    
    }
}
*/

//아래 풀이는 다음경우에 error 발생 
// Input : [2147483647] -> Output : true 이여야 하는데 false 가 나옴. 
// [2147483647] <-- 이 값이 Integer.MAX_VALUE 이기 때문. 

//Approach#1 - Top-down DFS
/*
class Solution {
    public boolean isValidBST(TreeNode root) {
        
        if(root == null){
            return false;
        }
        
        int leftValue = Integer.MIN_VALUE;
        int rightValue = Integer.MAX_VALUE;
        
        return validate(root, leftValue, rightValue);
        
    }
    
    boolean validate(TreeNode root, int leftValue, int rightValue){
        
        if(root == null){ // there is no node
            return true;
        }
        
        if((leftValue >= root.val) || (root.val >= rightValue)){
            return false;
        }
        
        if(!validate(root.left, leftValue, root.val)){
            return false;
        }
        
        if(!validate(root.right, root.val, rightValue)){
            return false;
        }
        
        return true;
    }
}
*/
