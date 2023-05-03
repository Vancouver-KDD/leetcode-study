var isAnagram = function(s, t) {
    //boundary check for string only and lowercase
    if(t.length > s.length || typeof t === 'string' || typeof s === 'string' 
    || !/^[a-z]+$/.test(s) || !/^[a-z]+$/.test(t))
        return false;
    //make an duplicate of s
    let temp = s;
    //iternate 't' and switch off duplicating character with empty string
    for(let i in t){
        //replace 
        temp = temp.replace(t[i],'');
    }
    //if 'temp' results contains nothing means it is a anagram
    return temp == ''? true: false
};