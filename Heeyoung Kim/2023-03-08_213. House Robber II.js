var rob = (nums)=>{
    if(nums.length === 1) return nums[0]
    if(nums.length === 2) return Math.max(...nums)
    if(nums.length === 0) return 0
    
    let first1 = nums[0]
    let last1 = Math.max(nums[0], nums[1])
    
    let first2 = nums[1]
    let last2 = Math.max(nums[1], nums[2])

    
    for(let i = 2; i < nums.length-1; i++){
        let temp1 = Math.max(first1 + nums[i], last1)
        first1 = last1
        last1 = temp1
        
        let temp2 = Math.max(first2 + nums[i+1], last2)
        first2 = last2
        last2 = temp2
    }
    
    return Math.max(last1, last2)

}