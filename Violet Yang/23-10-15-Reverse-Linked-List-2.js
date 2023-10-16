var reverseBetween = function(head, left, right) {
  var newHead = new ListNode(0);
  var now = newHead;
  var tmp = null;
  var reverseLast = null;
  var reverseHead = null;
  var reverseNow = null;
  var i = 0;

  newHead.next = head;

  while (now) {
    tmp = now.next;

    if (i === left - 1) {
      reverseHead = now;
    }

    if (i === left) {
      reverseLast = now;
      reverseNow = now;
    }

    if (i > left && i <= right) {
      now.next = reverseNow;
      reverseNow = now;
    }

    if (i === right) {
      reverseLast.next = tmp;
      reverseHead.next = reverseNow;
    }

    now = tmp;
    i++;
  }

  return newHead.next;


};