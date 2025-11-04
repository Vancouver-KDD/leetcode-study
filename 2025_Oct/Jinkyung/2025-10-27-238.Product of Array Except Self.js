class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let befor = Array(nums.length).fill(1); //=> [1,1,1,1]
    let after = Array(nums.length).fill(1); //=> [1,1,1,1]
    let output = []
    for(let i=0;i<nums.length;i++){
        if(i==0) befor[i]=1
        befor[i+1]=befor[i]*nums[i]
    }

    for(let j=nums.length-1;j>=0;j--){      
        after[j-1]= after[j]*nums[j]
    }

    for(let k=0;k<nums.length;k++){
        output[k]=befor[k]*after[k]
    }
    return output

    }
}


/**
nums = []
return answer[]

32-bit integer
         _ 
input=[1,2,3,4]
use Culcumative 
before left -> right 
[1,1*1,1*1*2,1*1*2*3] = [1,1,2,6]
after right->left
unshift input[2*3*1*4,3*1*4, 1*4,1] =[24,12,4,1]
output = [2*3*4*,1*3*4,1*2*4,1*2*3] =[24,12,8,6]

 */