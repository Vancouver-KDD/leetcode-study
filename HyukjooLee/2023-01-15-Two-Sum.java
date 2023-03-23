/**
 * Given an array of integers nums and an integer target, 
 * return indices of the two numbers such that they add up to target.
 */

// review
// integer array 와 target number 가 주어지고
// 어레이 안에 있는 두개의 element 를 선택하여 이를 더한 값이 타겟이 되는 경우
// 두개의 element의 위치, 즉 index 를 반환하는 문제

// 처음 문제를 받고 일치하지 않으면 무엇을 반환해야 하는지 물어볼 수 있음
// Should the function return null or an empty array in this case if there is no pair of values that meet the requirement?

// 먼저 간단하게 brute force 로 구현
// nested loop을 사용하여 각 숫자 쌍을 더하고 타겟과 비교하여 결과를 도출
// 배열 nums의 각 요소 nums[i]를 반복
// nums[i]에 대해 nums[j] = nums[i+1]부터 시작하여 배열의 나머지 요소를 반복
// nums[i] + nums[j] == target인지 확인
// if so, 해당 인덱스를 new int[] {i, j} 로 반환
// 중첩된 루프를 사용하여 배열의 각 숫자 쌍을 비교 => time O(N^2)
// store the indices of the two numbers that add up to the target => space O(1)

// 1. simple solution - brute force approach
// time complexity is O(N^2) as we iterate the array twice starting with the different index
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0; i < nums.length; i++) {
            for(int j = i + 1; j < nums.length; j++) {
                if(target == nums[i] + nums[j]) {
                    return new int[] {i,j};
                }
            }
        }
        return null;
        // return new int[0]; // return an empty array instead of null
    }
}


// 2. using HashMap

// 배열의 각 요소를 저장하는 해시 맵을 만드는 것으로 시작
// key will store a value positioned at the current index 
// value will store target - current
Map<Integer, Integer> map = new HashMap<>();

for(int i = 0; i < nums.length; i++) {
    int current = nums[i];
    // we can say a candidate value; compliment 'x' = target - current
    // x + current = target   
    int x = target - current;
    // 해시 맵에 'x' 가 포함되어 있는지 확인
    // 목표 값에 더해지는 배열의 두 숫자에 해당하는 한 쌍의 인덱스를 확인 가능
    if(map.containsKey(x)) return new int[] {map.get(x), i};
    // 'x' 가 맵에 포함되어 있지 않으면 현재 요소 'cur'와 해당 인덱스 'i'를 해시 맵에 추가
    map.put(current, i);
}

return new int[0];

// index 0 
nums:[2,7,11,15]
current:2
x=7
target:9
map:{2,0}

// index 1
nums:[2,7,11,15]
current: 7
x: 2
map:{2:0}
index of 2 => 0(value)
// index of 2 = 0 and current index =1 
[0,1]