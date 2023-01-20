// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
// You must write an algorithm that runs in O(n) time.
// Example 1:
// Input: nums = [100,4,200,1,3,2]
// Output: 4
// Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
// Example 2:
// Input: nums = [0,3,7,2,5,8,4,6,0,1]
// Output: 9

// 1. Approach : sort method 사용 | Greedy Search 알고리즘 사용

var longestConsecutive = (nums) => {
    if(nums.length === 0) return 0;
    //exception
  nums.sort((a,b) => a-b);
   
 return search(nums);
};

var search = (nums) => {
 let count = 1;
 let maxcount = 1;
 
 for(let i=1; i<nums.length; i++) {
   const isPrevDuplicate = nums[i-1] === nums[i];
   if(isPrevDuplicate) continue;
   //중복 원소일 경우 그냥 계속 이어가기 (exception)
   const isStreak = nums[i] === (nums[i-1] + 1);
   if(isStreak) {
     count++;
     continue;
   }
   
   maxcount = Math.max(maxcount, count);
   count = 1;
 }
 
 return Math.max(maxcount, count);
};


//Sort() Method 를 사용한 case (엔진에 따라 작용되는 sort 방식이 다름 주의!)
//Sort() Method => Tim sort = Insertion Sort + Merge Sort 
//시간 복잡도는 O(n) 평균은 O(log N) 

//Time Complexity : O(n) In the function search, there is one loop and travels all element.
//Space Complexity : O(n) Extra Space because of sort() method 


// 2. Approach : sort method 를 직접 구현 한다면?

var longestConsecutive = (nums) => {
    if(nums.length === 0) return 0;
    //exception
    heapSort(nums);
   console.log(nums);
 return search(nums);
};

var search = (nums) => {
 let count = 1;
 let maxcount = 1;
 
 for(let i=1; i<nums.length; i++) {
   const isPrevDuplicate = nums[i-1] === nums[i];
   if(isPrevDuplicate) continue;
   //중복 원소일 경우 그냥 계속 이어가기 (exception)
   const isStreak = nums[i] === (nums[i-1] + 1);
   if(isStreak) {
     count++;
     continue;
   }
   
   maxcount = Math.max(maxcount, count);
   count = 1;
 }
 
 return Math.max(maxcount, count);
};

// HeapSort() =>추가적인 메모리 사용이 필요하지 않다. (Heapify 정렬의 경우)
// 최선과 최악의 경우 모두 O(nlogn)의 시간 복잡도를 가진다.
// 불안정 정렬이며, 배열의 넓은 범위에 접근하게 되므로 참조 지역성이 좋지 못하다.

function heapSort(array) {
    // 초기 최대 힙 구현.
    for (let i = array.length - 1; i >= 0; i--) {
        heapify(array, array.length - 1, i);
    }

    // 최대의 크기를 가진 루트 노드를 리프 노드로 옮긴 뒤, 갱신된 위치를 제외하고 다시 최대 힙 구현.
    for (let i = array.length - 1; i >= 1; i--) {
        swap(array, 0, i);
        heapify(array, i - 1);
    }
}
function heapify(array, length, idx = 0) {
    while (true) {
        const leftChild = idx * 2 + 1;
        const rightChild = idx * 2 + 2;

        if (length >= rightChild) {
            // 자식 노드가 두 개일 경우 더 큰 노드와 비교 (최대 힙)
            const maxChild = (array[leftChild] < array[rightChild]) ? rightChild : leftChild;
            if (array[idx] < array[maxChild]) {
                swap(array, idx, maxChild);
                idx = maxChild;
            } else {
                break;
            }
        } else if (length === leftChild) {
            // 자식 노드가 하나인 경우 해당 자식과 비교.
            if (array[idx] < array[leftChild]) {
                swap(array, idx, leftChild);
            } else {
                break;
            }
        } else {
            // 리프 노드라면 정렬 종료.
            break;
        }
    }
}

function swap(array, aIdx, bIdx) {
    const temp = array[aIdx];
    array[aIdx] = array[bIdx];
    array[bIdx] = temp;
}

