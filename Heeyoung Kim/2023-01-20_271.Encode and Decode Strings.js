// Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

// Please implement encode and decode


var encode = (strs, sb = []) => {
    for (const str of strs) {
        const code = str.length.toString(2).padStart(8,'0');
        const encoding = `${code}${str}`;
        sb.push(encoding); 
    }
    return sb.join(''); 
}

var decode = (str, output = []) => {
    for (let left = 0, right = (left + 8),length = 0; left < str.length; left = (right + length), right = (left + 8)) {    
        const countString = str.slice(left, right);        
        length = parseInt(countString, 2);
        const decoding = str.slice(right, (right + length));    
        output.push(decoding);                    
    }

    return output;
}


// 이건 아무리 봐도 이해가 안간다.....
