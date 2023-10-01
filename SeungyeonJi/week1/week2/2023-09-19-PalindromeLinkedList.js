var isPalindrome = function (head) {
  let arr = [];

  while (head) {
    arr.push(head.val);
    head = head.next;
  }

  let end = arr.length - 1;

  for (let i = 0; i < arr.length / 2; i++) {
    if (arr[i] !== arr[end]) return false;
    end--;
  }
  return true;
};
