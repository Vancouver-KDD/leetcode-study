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

//2023-10-09
//idea : left 직전의 node 를 저장해 놓고, left 부터 right 까지 revrse order 만든뒤 
//        reversed link의 tail 이 right 다음의 node 를 가르키고, left 전의 node 가  reversed link 의 node 를 가르키도록 만듬.
//Time Complexity: O(N)
//Space Complexity: O(1)
//위의 idea 로 내가 만든 solution 
/*
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        
        if(head == null || head.next == null){
            return head;
        }
        
        ListNode leftLeftNode = null;
        ListNode currNode = head;
        int count = 1;
        while(count < left){
            leftLeftNode = currNode;
            currNode = currNode.next;
            count++;
        }
        
        ListNode endNode = currNode; //save the end of reversed linked list
        ListNode prevNode = null;
        while(count <= right){
            ListNode nextNode = currNode.next;
            currNode.next = prevNode;
            prevNode = currNode;
            currNode = nextNode;
            count++;
        }
        
        endNode.next = currNode;
        ListNode startNode = prevNode;
        
        if(leftLeftNode == null){
            return startNode;
        }
        
        leftLeftNode.next = startNode;
        return head;
        
    }
}
*/
//위의 idea 로 leetcode solution이 만든 조금더 깔끔하게 정리된 코드 
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        
        if(head == null || head.next == null){
            return head;
        }
        
        ListNode dummy = new ListNode(0, head);
        ListNode before = dummy;
        
        int count = 1;
        while(count < left){
            before = before.next;            
            count++;
        }
        
        ListNode prev = null;
        ListNode curr = before.next;
        while(count <= right){
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
            count++;
        }
        
        before.next.next = curr; //before.next: tail of reversed list / curr: after of reversed list
        before.next = prev; //prev : head of reversed list
        
        return dummy.next;
    }
}


//recursive solution - my idea 
//아래 leetcode 의 recursive 솔루션이 전역변수를 두어 해결하였는데, 
// 전역변수를 들거면 '206. Reverse Linked List' 의 방법을 이용해도 될거 같아서 그렇게 해본 내용
//leetcode 의 내용보다 이방법이 더 이해하기가 쉬움. 
/*
class Solution {
    ListNode after = null;
    
    public ListNode reverseBetween(ListNode head, int left, int right) {
        
        if(head == null || head.next == null){
            return head;
        }
        
        ListNode dummy = new ListNode(0, head);
        ListNode before = dummy;
        int count = 1;
        while(count < left){
            before = before.next;
            count++;
        }
        
        ListNode reversedHead = recursiveReverse(before.next, right -left);
        before.next = reversedHead;
        
        return dummy.next;
        
    }
    
    ListNode recursiveReverse(ListNode head, int count){
        if(head.next == null || count == 0){
            after = head.next;
            return head;            
        }
        
        ListNode nextNode = head.next;
        ListNode reversedHead = recursiveReverse(nextNode, count -1);
        nextNode.next = head;
        head.next = after;
        return reversedHead;
    }
}
*/
//recursive solution -leetcode solution- 복잡함. 
/*
class Solution {

    // Object level variables since we need the changes
    // to persist across recursive calls and Java is pass by value.
    private boolean stop;
    private ListNode left;

    public void recurseAndReverse(ListNode right, int m, int n) {

        // base case. Don't proceed any further
        if (n == 1) {
            return;
        }

        // Keep moving the right pointer one step forward until (n == 1)
        right = right.next;

        // Keep moving left pointer to the right until we reach the proper node
        // from where the reversal is to start.
        if (m > 1) {
            this.left = this.left.next;
        }

        // Recurse with m and n reduced.
        this.recurseAndReverse(right, m - 1, n - 1);

        // In case both the pointers cross each other or become equal, we
        // stop i.e. don't swap data any further. We are done reversing at this
        // point.
        if (this.left == right || right.next == this.left) {
            this.stop = true;            
        }

        // Until the boolean stop is false, swap data between the two pointers
        if (!this.stop) {
            int t = this.left.val;
            this.left.val = right.val;
            right.val = t;

            // Move left one step to the right.
            // The right pointer moves one step back via backtracking.
            this.left = this.left.next;
        }
    }

    public ListNode reverseBetween(ListNode head, int m, int n) {
        this.left = head;
        this.stop = false;
        this.recurseAndReverse(head, m, n);
        return head;
    }
}
*/
