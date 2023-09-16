/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let iterations = nums.length;

    for(let i = 0; i < iterations; i++){
        nums[i] *= nums[i];
    }

    quick(nums, 0, iterations-1);

    return nums;
};

function partition(array, left, right){
    let p = array[Math.floor((right + left)/2)];
    let i = left;
    let j = right;

    while(i <= j){
        while(array[i] < p){
            i++;
        }
        while(array[j] > p){
            j--;
        }

        if(i <= j){
            let temp = array[i];
            array[i] = array[j];
            array[j] = temp;
            i++;
            j--;
        }
        return i;
    }
};

function quick(array, left, right){
    let index;
    if(array.length > 1){
        index = partition(array, left, right);

        if(left < index-1){
            quick(array, left, index-1);
        }

        if(index < right){
            quick(array, index, right)
        }
    }
    return array;
};