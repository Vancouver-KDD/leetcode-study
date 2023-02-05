// Given the head of a singly linked list, 
// reverse the list, and return the reversed list.

// prev 노드는 전 노드를 추적할거고
// current 는 리스트를 순환하기 위한
// temp 는 current 의 다음 노드를 일시적으로 저장하기 위해 사용

//       [null -> 1 -> 2 -> 3 -> null]
//        prev   cur                   (0) initialize

//        prev   cur  temp             (1) 다음 노드를 추적하기 위한 temp 생성 (current.next)

//            <-                       (2) 포인터 reverse (current.next = prev)   

//               prev                  (3) 다음 loop 에서 전 노드 추적하기 위한 prev node 이동 (current)

//                     cur             (4) cur 노드 이동 (temp)

// 1. using 3 pointers ; current, prev, temp 
// to keep track of nodes to update reserved node
// time complexity is O(N) as  we visit each node in the linked list (linear)

// Follow up: A linked list can be reversed either iteratively or recursively.
// Could you implement both?
public ListNode reverseList(ListNode head) {
        // initialize current and prev node // 0
        ListNode current = head;
        ListNode prev = null;
        while(current != null) {

            // temporaily store the next node of current node
            ListNode temp = current.next; // 1

            // change pointer from -> to <- 
            current.next = prev;          // 2

            // move prev node to current node
            prev = current;               // 3

            // move current node to temp node
            current = temp;               // 4
        }
        // finally store and return prev as it will point to the head of reversed list
        head = prev;
        return head;
}

// 2. using resursion - 호출 스택을 사용하기 때문에 space complexity 를 고려 해봤을 때
// 첫 솔루션는 O(1) 로 낫다고 할 수 있다?
// we find the reversed linked list of the head.next node
// then adjust the pointers of the current node and the next node to reverse the current node.
// the head of the reversed linked list is returned.
public ListNode reverseList(ListNode head) {
	if(head == null || head.next == null) {
		return head;
	}
	ListNode result = reverseList(head.next);
	head.next.next = head;
	head.next = null;
	return result;
}