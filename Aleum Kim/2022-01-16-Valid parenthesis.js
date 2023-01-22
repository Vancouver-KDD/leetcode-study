// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.

var isValid = function(s) {
    let bracket = {
     '[':']',
     '{':'}',
     '(':')'
 }
let heap = [];

for(let char of s){
if(bracket[char]) {
  heap.push(bracket[char])
} else{
 if(heap.pop() !== char) return false
}
}
return (!heap.length)

};

var isValid = function(s) {
    if(s == "") {
        return true;
    }
    if(s.length <2) {
        return false;
    }
    const pairBrkts = {
        "{" : "}",
        "(" : ")",
        "[" : "]"
    }
    let stk = [];
    let arr = s.toString().split("");

    for(let i = 0; i< arr.length; i++) {
        let br = arr[i];
        if(pairBrkts[br]) {
            stk.push(br);
        }
        else {
            let chkBr = stk.pop();
            if(pairBrkts[chkBr] !=br) {
                return false;
            }
        }
    }


if(stk.length >0) {
    return false;
}
return true;
}