/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

//Queue 에 null 을 안쓰고 하는 경우 
//Time Complexity: O(N)
//Space Complexity: O(N)

class Solution {
    public Node connect(Node root) {
                if(root == null){
            return null;
        }
         
        Queue<Node> bfsQueue = new LinkedList<>();
        bfsQueue.add(root);        
       
        while(!bfsQueue.isEmpty()){
           
            int size = bfsQueue.size();
            Node prev = null;
            for(int i = 0; i < size; i++){
                Node leave = bfsQueue.remove();
                if(prev != null){
                    prev.next = leave;                    
                }
                
                if(leave.left != null){
                    bfsQueue.add(leave.left);
                }
                if(leave.right != null){
                    bfsQueue.add(leave.right);
                }   
                prev = leave;
            }
        }
            
        return root;
    }
}


//Queue 에 null 을 넣어서 하는 경우 
//Time Complexity: O(N)
//Space Complexity: O(N)
/*
class Solution {
    public Node connect(Node root) {
        if(root == null){
            return null;
        }
         
        Queue<Node> bfsQueue = new LinkedList<>();
        bfsQueue.add(root);
        bfsQueue.add(null);
        
        Node prev = null;
        
        //queue: (1, null)->(null, 2, 3, null)->(2,3,null)->(3,null,4,5)->(null,4,5,6,7,null)
        //      ->(4,5,6,7,null)->(5,6,7,null)->(6,7,null)->(7,null)->(null,null)->(null)->()
        //prev: null, 1,null, 2,3,null,4,5,6,7,null
        //leave: 1, null, 2,3,null,4,5,6,7,null,null
        //endR: true
        //next: 1->null,2->3->null,4->5->6->7->null
        while(!bfsQueue.isEmpty()){
            Node leave = bfsQueue.remove();
            if(prev != null)
            {
                prev.next = leave;
            }           
            prev = leave;
            
            if(leave == null){
                continue;
            }
            
            boolean endRight = false;
            
            if(bfsQueue.peek() == null){ // it means that current leave is end of right in this level
                endRight = true;
            }
                
            if(leave.left != null){ //bottom level node 때문에 필요 
                bfsQueue.add(leave.left);
            }
            if(leave.right != null){ //bottom level node 때문에 필요  
                bfsQueue.add(leave.right);
            }
            if(endRight){
                bfsQueue.add(null);
            }

        }
            
        return root;
    }
}
*/

//idea2:  Using previously established next pointers (leetcode solution)
// 이 문제에 한해서는 이 방법이 가장 최적의 solution 임. 
// (궁금증: full binary tree 라서 가능한 솔루션일까??? )
/*
 leftmost = root
 while (leftmost.left != null)
 {
     head = leftmost
     while (head != null)
     {
         1) Establish Connection 1
         2) Establish Connection 2 using next pointers
         head = head.next
     }
     leftmost = leftmost.left
 }
*/
// Time Complexity: O(N)
// Space Complexity: O(1)
/*
class Solution {
    public Node connect(Node root) {
        if(root == null){
            return null;
        }
        
        Node leftMost = root;
        
        //[1,2,3,4,5,6,7]
        //leftMost:1, 2, 4
        //leftMost.left:2, null
        //head:1, 2, 3
        //next: 2->3, 4->5->6->7
        
        while(leftMost.left != null){
            Node head = leftMost;
            
            while(head != null){
                if(head.left != null){
                    head.left.next = head.right;
                }
            
                if(head.next != null){
                    head.right.next = head.next.left;
                } 
                head = head.next;
            }
            leftMost = leftMost.left;
        }
        
        
        return root;
    }
}
*/
