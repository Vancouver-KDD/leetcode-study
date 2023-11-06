var findTheDifference = function(s, t) {
    if(!s.length){
       return t
    }
 
    let newObj = {}
    for (const el of t) {
       if(newObj[el]){
          newObj[el] += 1
       }else {
          newObj[el] = 1
       }
    }
 
    for(let i = 0; i < s.length; i++){
       if(Object.keys(newObj).includes(s[i])) {
          newObj[s[i]] -= 1
       }
       
    }
    return Object.keys(newObj).find((key) => newObj[key] == 1)
 };