
var removeNthFromEnd = function(head, n) {
    let dummyhead = {next:head};
    console.log(dummyhead);
    let slow = dummyhead;
    let fast = dummyhead;
    
    // 두 포인터의 간격을 n 만큼 벌려준다. 
    for(let i=1; i<= n; i++){
        fast = fast.next;
    }
    
    while(fast.next) {
        slow = slow.next;
        fast = fast.next;
        console.log(slow, fast);
    }
    
    slow.next = slow.next.next //slow.next 를 slow | N | fast 이 상황에서 slow.next.next 즉 fast 즉 last node 를 지정해준다. 
    return dummyhead.next; //그러면 자동스럽게 해당 n 번째 요소는 삭제가 된 dummyhead 를 얻을 수 있다. 
};


//Time complexity : O(N) We traverse thru the Linked List once.
//Space Complexity : O(1) We always use two nodes, regardless of size of Linked List

