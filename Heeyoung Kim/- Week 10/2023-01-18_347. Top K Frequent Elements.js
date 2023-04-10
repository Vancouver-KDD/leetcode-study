// 347. Top K Frequent Elements

// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
// Example 1:

// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]
// Example 2:

// Input: nums = [1], k = 1
// Output: [1]


//1. Approach : Sorted Hashmap() => Error "Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size."

var topKFrequent = function(nums, k) {
  
    let map ={};
    let result = [];
   
    
    for(let i=0; i<nums.length; i++) {
        // if(map[nums[i]]) { map[nums[i]] = map[nums[i]]+1; }
        // else { map[nums[i]] == 1;}
        map[nums[i]] = map[nums[i]] + 1 || 1;
    }
   
    let keys = Object.keys(map);
    
    keys.sort((a,b) => {return map[a]-map[b]});
    
    while(result.length < k) {
        result.push(keys.pop());
    }
    
    return result;
};


//Time Complexity : Using the hashmap as data structure, This step takes O(N) time where N is a number of elements in the list.
//Space Complexity : O(n) Extra Space for Array 


// //2. Approach : Min-Heap
// var topKFrequent = function(nums, k) {
//     const isOverCapacity = k === nums.length;

//     const map = buildmap(nums);
//     console.log(map);
//     const minHeap = minheap(map,k);
//     console.log(minHeap);

//     return getTopKarray(minHeap, k);

// }

// const buildmap = (nums, map = new Map())=>{
//    for(let i =0; i<nums.length; i++) {
//     map[nums[i]] = map[nums[i]] + 1 || 1;
//    }

//    return map;
// }
// // Build Hashmap O(N)

// const minheap = (map, k) =>{
//     const minHeap = new MinPriorityQueue({priority: ([num, count]) => count});

//     for(const [num,count] of map.entries()) {
//         minHeap.enqueue([num, count]);
//         const isOverCapacity = k < minHeap.size();
//         if(isOverCapacity) minHeap.dequeue();
//     }

//     return minHeap;
// }
// // Build MinHeap of k most frequent element (O(NlogK))

// const getTopKarray = (minHeap, k, topK = []) => {
//     for (const count of bucket) {/* Time O(N) */
//         for (const num of count) {   /* Time O(N) */
//             const isAtCapacity = topK.length === k;
//             if (isAtCapacity) break;

//             topK.push(num);               /* Space O(K) */
//         }
//     }

// return topK;
// }

// //Build an output array (O(logN))

// // Time Complexity : O(NlogK)
// // Space Complexity : O(N+K)