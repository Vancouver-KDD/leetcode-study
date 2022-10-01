//2022-09-24 모르겠다.봐도 이해가 잘 안간다.

var threeSum = function(array) {
     array.sort((a,b) => a - b);
    const triplets = [];

    for(let i=0; i < array.length - 2; i++){
        if(array[i] != array[i-1]){ // making sure our solution set does not contain duplicate triplets
            let left = i + 1;
          let right = array.length - 1;

            while (left < right){
                const currentSum = array[i] + array[left] + array[right];
                if (currentSum === 0){
                    triplets.push([array[i], array[left], array[right]]);
                    while(array[left] == array[left + 1]) left ++
                    while(array[right] == array[right - 1]) right -- // making sure our solution set does not contain duplicate triplets
                    left ++;
                    right --;
                } else if(currentSum < 0) {
                    left ++
                } else if(currentSum > 0){
                    right --
                }
            }
        }
    }
    return triplets
};
