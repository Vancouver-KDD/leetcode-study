var isValid = function(s) {
    if(!s || s.length < 1) return false
    
    // check if the string length is even number
    // if not, it means one of them doesn't have pair
    if(pair.length % 2 === 1) return false

    // Stack - to push and pop in the correnct order to match items
    const pair = []
    
    // loop through the string char
    for (let i = 0; i < s.length; i++) {
        // if char is opening braket, push pair closing braket to array(stack)
        if (s[i] === "(") {
        	pair.push(")")
        }
        else if (s[i] === "{") {
        	pair.push("}")
        }
        else if (s[i] === "[") {
        	pair.push("]")
        }
        // if char is closing braket, compare with last item of pair array
        // if not same, then return false
        else if(s[i] !== pair.pop()) {
        	return false
        }
    }
    return true

    // complexity
    // time: O(n)
    // space: O(n)
};