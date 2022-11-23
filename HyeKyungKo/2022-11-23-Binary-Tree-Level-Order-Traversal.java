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
 //2022-11-22- Recursive 
//Time Complexity: O(N) 
//Space Complexity: O(N) : Max 일때가 tree depth 가 node 수만큼일때 - right child 만있거나 left child 만 있는경우 
 class Solution{
     public List<List<Integer>> levelOrder(TreeNode root){
         List<List<Integer>> resultList = new ArrayList<>();
        if(root == null){
            return resultList;
        }

        recursiveLevelVisit(resultList, root, 0);

         return resultList;
     }

     private void recursiveLevelVisit(List<List<Integer>> result, TreeNode root, int level){

         if(root == null){
             return;
         }
         if(result.size() <= level){
             result.add(new ArrayList<>());
         }
        result.get(level).add(root.val);
        recursiveLevelVisit(result, root.left, level+1);
        recursiveLevelVisit(result, root.right, level+1);

     }
 }
 //2022-11-22 - Iteration - Queue 만 사용한 경우 
 //Time Complexity: O(N)
//Space Complexity: O(N)
 /*
 class Solution{
     public List<List<Integer>> levelOrder(TreeNode root){
         List<List<Integer>> result = new ArrayList<>();
         if(root == null){
             return result;
         }
         Queue<TreeNode> queue = new LinkedList<>();
         queue.add(root);
         int level = 0;
         while(!queue.isEmpty()){
             result.add(new ArrayList<>()); //add new List. 
             int size = queue.size();
             for(int i = 0; i < size; i++){
                 TreeNode node = queue.remove();
                result.get(level).add(node.val);
                if(node.left != null){
                    queue.add(node.left);
                }
                if(node.right != null){
                    queue.add(node.right);
                }
             }
             level++;
         }

         return result;
     }
 }
 */
//2022-11-22 - Iteration - Queue 에다가 Pair<Key, Value> 클래스를 사용한 경우 
//Limitation : if root is null, return empty list;
//Input: root = [3,9,20,null,null,15,7] --> Output: [[3],[9,20],[15,7]]
//Time Complexity: O(N)
//Space Complexity: O(N)
/*
class Solution{
    public List<List<Integer>> levelOrder(TreeNode root){
        List<List<Integer>> result = new ArrayList<>();
        if(root == null){
            return result;
        }

        //Pair<Key, Value> : key is TreeNode, value is level
        Queue<Pair<TreeNode, Integer>> queue = new LinkedList<Pair<TreeNode, Integer>>();
        queue.add(new Pair(root, 1));
        while(!queue.isEmpty()){
            Pair<TreeNode, Integer> currPair = queue.remove();
            int level = currPair.getValue();
            if(result.size() < level){
                result.add(new ArrayList<Integer>());
            }
            TreeNode node = currPair.getKey();
            result.get(level-1).add(node.val);
            if(node.left != null){
                queue.add(new Pair(node.left, level+1));
            }
            if(node.right != null){
                queue.add(new Pair(node.right, level+1));
            }
        }
        return result;
    }
}
*/

//2022-09-22
//Limitation: if root is null, return  empty List;
// Input: root = [3,9,20,null,null,15,7] -> Output: [[3],[9,20],[15,7]]
// Input: root = [1] -> Output: [[1]]
// Input: root = [] -> Output: []
// Time Complexity: O(N), Space Complexity: O(N)

// leetCode 해법보고 update한 코드 1) recursive-- level 정보를 저장하기위해 따로 class 를 만들필요가 없음.
// Timecomplexity : O(n), SpaceComplexit: O(n)
/*
class Solution {
    
    List<List<Integer>> totalNodes = new ArrayList<List<Integer>>();   
    
    public List<List<Integer>> levelOrder(TreeNode root) {        
        
        if(root == null){
            return totalNodes;
        }
        
        recursiveCheck(root, 0);
        
        return totalNodes;
    }
    
    void recursiveCheck(TreeNode root, int level){
        
        int size = totalNodes.size(); // size means level
        
        if(size == level){
            totalNodes.add(new ArrayList<Integer>());
        }
        
        totalNodes.get(level).add(root.val);
        
        //process child nodes for the next level
        if(root.left != null){
            recursiveCheck(root.left, level+1);
        }
        if(root.right != null){
            recursiveCheck(root.right, level+1);
        }
    }
}
*/
// leetCode 해법보고 update한 코드 2) iteration-- level 정보를 저장하기위해 따로 class 를 만들필요가 없음.
// Timecomplexity : O(n), SpaceComplexit: O(n)
/*
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        List<List<Integer>> totalNodes = new ArrayList<List<Integer>>();
        
        if(root == null){
            return totalNodes;
        }
        
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        
        queue.add(root);
        //int level = 1;
        
        while(!queue.isEmpty()){
            
            List<Integer> levelNodes = new ArrayList<Integer>();
            int size = queue.size();
            
            //add child nodes for the next level
            for(int i = 0; i < size; i++){
                TreeNode node = queue.poll();                
                levelNodes.add(node.val);
                
                if(node.left != null){
                    queue.add(node.left);
                }
                if(node.right != null){
                    queue.add(node.right);
                }
            }
            
            totalNodes.add(levelNodes);
            
            //level++;
        }
        
        return totalNodes;
        
    }
}
*/
//처음 풀이한 코드 
/* 
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        List<List<Integer>> totalNodes = new ArrayList<List<Integer>>();
        
        if(root == null){
            return totalNodes;
        }
        
        Deque<LevelNode> queue = new ArrayDeque<LevelNode>();
        
        LevelNode levNode = new LevelNode(root, 0);
        queue.add(levNode);
        List<Integer> eachLevelNode = new ArrayList<Integer>();
       // eachLevelNode.add(root.val);        
        //totalNodes.add(eachLevelNode);
        int currentLevel = -1;
        
        while(!queue.isEmpty()){
            levNode = queue.poll();
            if(currentLevel != levNode.level){
                eachLevelNode = new ArrayList<Integer>();
                totalNodes.add(eachLevelNode);
                currentLevel = levNode.level;
            }
            eachLevelNode.add(levNode.node.val);         
            
            if(levNode.node.left != null){
                queue.add(new LevelNode(levNode.node.left, levNode.level+1));                
            }
            if(levNode.node.right != null){
                queue.add(new LevelNode(levNode.node.right, levNode.level+1));               
            }
        }
        
        return totalNodes;
    }
    
    class LevelNode{
        TreeNode node;
        int level;
        LevelNode(){
            node = null;
            level = 0;
        }
        LevelNode(TreeNode inputNode, int inputLevel){
            node = inputNode;
            level = inputLevel;
        }
    }
        
}
*/