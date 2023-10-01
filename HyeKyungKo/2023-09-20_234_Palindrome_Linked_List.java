/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

 //간단한 방법: ListNode 들의 val 을  ArrayList 에 넣고, check palindrome
 //  (주의점: node 자체가 아닌, node의 val 을 list 에 넣어야함. node 자체를 비교하면 안됨. )
 //Time Complexity: O(N)
 //Space Complexity: O(N)
 /*
class Solution{
    public boolean isPalindrome(ListNode head){
        if(head.next == null ){
            return true;
        }

        List<Integer> nodes = new ArrayList<>();
        ListNode currNode = head;
        while(currNode!=null){
            nodes.add(currNode.val); // node 의 val 이 palindrome 인지 아닌지 봐야한다. 
            currNode = currNode.next;
        }

        //check palindrome
        int left = 0;
        int right = nodes.size() -1;
        while(left < right){
            if(nodes.get(left)!= nodes.get(right)){ 
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}
*/
//Advanced 방법: <-- Space Complexity 를 O(1) 으로 하기
//1. 중간위치를 찾는다. - slow/fast 방법을 이용
//2. 중간위치 다음node부터 끝node 까지 reverse list 를 만든다. 
//3. reverse list 와 원래 list 를 같은지 비교 
//  3-1. 면접관에서 list 를 원상복귀 시켜야 하는지 묻고, 그래야 한다면 원상복귀 시키기 
//4. 결과 boolean 값 리턴 
//Time Complexity: O(N)
//Space Complexity: O(1)
class Solution{
    public boolean isPalindrome(ListNode head){
        if(head == null || head.next == null){
            return true;
        }

        //find mid position
        ListNode fast = head; //move 2 steps at a time
        ListNode slow = head; //move 1 step at a time
        //1->2->2->1->null
        //1->2->3->2->1->null
        while(fast.next != null && fast.next.next != null){ //check!!! 다른 fast/slow 는 fast !=null && fast.next !=null 이였는데 이건 다름. 
            fast = fast.next.next; //1->2 , 1->3->1
            slow = slow.next;   //1->2, 1->2->3
        }

        ListNode secondHalfHead = slow.next;
        //make reverse linked list;
        ListNode prev = null;
        ListNode next = null;
        while(secondHalfHead != null){
            next = secondHalfHead.next;
            secondHalfHead.next = prev;
            prev = secondHalfHead;
            secondHalfHead = next;
        }
        
        secondHalfHead = prev;
        //input linked list 를 원상복귀 할 필요가 없는 경우 
        /*
        while(secondHalfHead != null){
            if(secondHalfHead.val != head.val){
                return false;
            }
            secondHalfHead = secondHalfHead.next;
            head = head.next;
        }
        return true;
        */
        //input linked list 를 원상복귀 해야하는 경우. 원상복귀 해야하니 temparary ListNode 선언필요
        boolean result = true;
        ListNode firstList = head;
        ListNode secondList = secondHalfHead;
        while(result && secondList != null){
            if(secondList.val != firstList.val){
                result = false;
            }
            secondList = secondList.next;
            firstList = firstList.next;
        }

        //make reverse linked list
        prev = null;
        next = null;        
        while(secondHalfHead != null){
            next = secondHalfHead.next;
            secondHalfHead.next = prev;
            prev = secondHalfHead;
            secondHalfHead = next;
        }        
        slow.next = prev; //firstHalfLast points secondHalfHead
        return result;
    }
}



//Limitation: head is null, -> output: return false??
//Time complexity: O(N), Space complexity: O(N)
/*
class Solution {
    public boolean isPalindrome(ListNode head) {
        if(head == null){
            return false;
        } 
        if(head.next==null){ //there is only 1 node.
            return true;
        }
        
        //first check the numbe of linkedlist 
        ListNode node = head;
        int length = 0;
        while(node != null){
            length++;
            node = node.next;
        }

        //put the half of linked list nodes to stack and then compare it with other half of linked list of node
        //how can I distinguish even number of length and odd number of length 
        // mid  = length / 2   (5/2) = 2,  4/2 = 2
        // even: from node1 to node(mid) , from node(mid) to end
        //odd : from node(1) to node(mid), from node(mod+2 to end)
        Deque<Integer> stack = new ArrayDeque<Integer>();
        int count =1;
        int mid = length/2;
        node = head;
        while(count <= mid){
            stack.push(node.val);
            node = node.next;
            count++;
        }
        if( length % 2 != 0){
            node = node.next;
        }
        
        while(node != null){
            if(stack.isEmpty()){
                return false;
            }
            int val = stack.pop();
            if(val != node.val){
                return false;
            }
            
            node = node.next;
        }
        
        return true;
        
    }
    

}


/*
class Solution {
    public boolean isPalindrome(ListNode head) {
        
        if(head == null){
            return true;
        }
        
        List<Integer> list = new ArrayList<>();
        
        ListNode nextNode = head;
        while(nextNode != null){
            list.add(nextNode.val);
            nextNode = nextNode.next;
        }
        
        return checkPalindrome(list);
    }
    
    private boolean checkPalindrome(List<Integer> list){
        
        if(list.size() <= 1){
            return true;
        }
        
        int left = 0;
        int right = list.size() -1;
        
        while(left < right){
            
            //System.out.println("left:right = " +left + ":" + right);
            if(list.get(left) != list.get(right)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
*/