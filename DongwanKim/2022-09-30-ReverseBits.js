var reverseBits = function(n) {
    let ans = 0;
    
    for(let i=0; i<32; i++){
        let bit = (n >>> i) & 1;
        ans = (ans | (bit << (31-i)) >>> 0) >>> 0

    }
    return ans
};