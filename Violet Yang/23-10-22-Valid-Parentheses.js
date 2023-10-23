ar isValid = function(s) {
    const map = new Map()
    map.set("[","]")
    map.set("(",")")
    map.set("{","}")

//[{()}], () [] {}
    let stack = []
    if(s.length % 2 !==0){
        return false
    }
    for(let i = 0; i < s.length; i++){
       if(map.get(s[i])){// (=> ) , ], }, ), undefined
           stack.push(map.get(s[i])) // [)]
           
       }else {
           if(stack[stack.length-1] === s[i]){
                stack.pop()
           }else {
               return false
           }

       }
    }
                       
    if(!stack.length){
        return true
    }else {
         return false
    }
};