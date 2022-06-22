var getSum = function(a, b) {
    var sum = a^b; 
    var carry = (a&b) << 1;
    
    while (carry != 0){
        var temp = sum;
        sum = sum ^ carry;
        carry = (temp&carry) << 1;
    }
    
    return sum;
};
