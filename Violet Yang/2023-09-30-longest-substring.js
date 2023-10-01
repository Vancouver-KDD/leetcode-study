var longestSubstring = function(s, k) {
    // sort
    // count repeated value
    const arr = s.split('') // ['adbdd']
    // a = 3, b = 2 ...
    // if(count < k) -> break
    // {a : 1, b : 3, c : 5...}
    
    const newObj =  arr.reduce((acc, cur) => {
        acc[cur] =  (acc[cur] || 0) + 1
        console.log(acc)
        return acc
    }, {})
    const cntArr = Object.values(newObj).filter(el=> el>= k)
    const sum = cntArr.reduce((acc,cur)=> {
        return acc += cur
    },0)
    return sum
};