//initial solution.. ㅠㅠ
var rotateRight = function (head, k) {
    if (!head) return head;
    if (k === 0) return head;

    let len = 1;
    let tmp = head;

    if (tmp) {
        while (tmp.next) {
            len++;
            tmp = tmp.next;
        }
    }

    k = k % len;

    let tmpHead = head;
    let tmpCut = head.next;
    let newHead = head;
    let result = head;
    for (let i = 1; i < len; i++) {
        if (i < len - k) {
            tmpHead = tmpHead.next;
            tmpCut = tmpHead.next;
        } else if (i === len - k) {
            tmpHead.next = null;
            newHead = tmpCut;
            result = newHead;
        } else {
            newHead = newHead.next;
        }
    }
    if (newHead && k !== 0){
        newHead.next = head;
    }
    
    return result;
};