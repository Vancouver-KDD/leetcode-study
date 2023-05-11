var hasCycle = function(head) {
    if (!head) return false

    // HashMap to track occured node
    let history = new Set()

    // loop while current node has next node
    while(head.next) {
        // if node of next node has occured 
        // hashmap loopup is O(1)
        if(history.has(head.next)) return true
        // if node has not occured before, add to history
        history.add(head)
        // go to next node
        head = head.next
    }

    // return false, means one of the node's next is null so it's not cycle
    return false

    // complexity
    // time: O(n)
    // space: O(n) -> using hashmap
};

// reference: https://leetcode.com/problems/linked-list-cycle/solutions/2689992/javascript-short-and-sweet-while-loop-92-fast/?languageTags=javascript
// improve Space Complexity - but not good if want to keep the original value of nodes
var hasCycle = function(head) {
    if (!head) return false

    // loop while current node has not occured
    // if node value is 'checked', means it has occured before, so return true
    while(head.value != 'checked') {
        // change node value to 'checked'
        head.value = 'checked'
        // move to next
        head = head.next
        // if one of the node's next was null, head will be null
        // if the case return false
        if (!head) return false
    }

    return true

    // complexity
    // time: O(n)
    // space: O(1)
};