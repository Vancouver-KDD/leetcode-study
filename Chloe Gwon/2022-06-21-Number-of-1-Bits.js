var hammingWeight = function(n) {
    var result = 0;
    while (n != 0){
        result += n%2;
        n = n >>> 1;
    }
    return result;
};

//Be careful! '>>' and '>>>' is different. 
