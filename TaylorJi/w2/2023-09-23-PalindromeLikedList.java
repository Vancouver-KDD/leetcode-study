class Solution {
    public boolean isPalindrome(ListNode head) {
        // edge case, null check
        if(head == null) {
            return true;
        };
        // curr pointer
        ListNode curr = head;
        boolean isPal = true;
        // stack to store node's value (from head to the end of the linked list)
        Stack<Integer> st = new Stack<Integer>();
        while (curr != null) {
            st.push(curr.val);
            curr = curr.next;
        }
        // compare the curr.val to st.pop
        while (head != null && !st.isEmpty()) {
            int i = st.pop();
            if (head.val == i) {
                isPal = true;
            } else {
                isPal = false;
                break;
            }
            head = head.next;
        }
        return isPal;
        
    }
      
    }