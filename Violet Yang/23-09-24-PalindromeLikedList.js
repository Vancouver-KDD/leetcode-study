
var isPalindrome = function (head) {

    let valuesFound = [];
    while (head) {
        valuesFound.push(head.val);
        head = head.next;
    }

 
    let left = 0;
    let right = valuesFound.length - 1;
    while (left <= right) {
        if (valuesFound[left] !== valuesFound[right]) {
            return false;
        }
        left++, right--;
    }

    return true;
};
