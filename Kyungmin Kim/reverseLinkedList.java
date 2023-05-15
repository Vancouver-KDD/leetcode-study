class Solution{
    public ListNode reverseList(ListNode head){
        return rev(head, null);
    }
    public ListNode rev(ListNode node, ListNode pre){
        if(node == null) return pre;
        ListNode temp = node.next;
        node.next = pre;
        return rev(temp, node);
    }
}