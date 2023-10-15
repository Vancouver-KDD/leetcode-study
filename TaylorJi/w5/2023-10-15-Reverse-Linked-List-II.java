class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        // edge case
        if(head.next == null){
            return head;
        }
        int size =0;
        // pointers
        ListNode temp = head;
        ListNode leftNode  = null;
        ListNode rightNode  = null;
        // arraylist to store the values
        List<Integer> arr = new ArrayList<>();
        while(temp != null ){
            size++; // 1,2,3,4  
            if(size == left){
                leftNode = temp; // 2
            }
            if(size >= left && size <= right){
                arr.add(temp.val); // 2, 3, 4
            }
            if(size == right){
                rightNode= temp; // 4
            }
            temp = temp.next; // 1, 2, 3, 4
        }
        int sizes = left; // 2
        // because index start from 0
        int arrSize = arr.size()-1;
        while(sizes <= right){
            leftNode.val = arr.get(arrSize--);
            leftNode = leftNode.next;
            sizes++;
        }


        return head;

    }
}