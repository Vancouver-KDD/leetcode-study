/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let hashMap={};
    let result=[];

    // frequeny counter map
    for(let num of nums){
        if(hashMap[num]){
            hashMap[num]++;
        }else{
            hashMap[num]=1;
        }
    }

    // sort by most frequent ones ( desc )
    let arr=Object.entries(hashMap); // Object.entries coverts object to array of arrays for sort

    arr.sort((a,b)=>{
        return b[1]-a[1] // a[1] or b[1] is the frequency value
    });


    // get the k most frequent ones , and push it to the final result
    arr.slice(0,k).forEach(element=> result.push(+element[0]));

    return result;
};
