/**
 * Given an integer array nums, return true if any value appears at least twice in the array,
 * and return false if every element is distinct.
 */

// 중복 되면 true, 중복되지 않으면 false


// 1. using nested loops; compare each element in the array to elements in the array
// time complexity is O(N^2) - would be useful when the size of array is small
class Solution {
    public boolean containsDuplicate(int[] nums) {
        // iterate each element in the array
        for(int i = 0; i < nums.length; i++) {
            // compare each element in the array to elements in the other array
            for(int j = i + 1; j < nums.length; j++) {
                // if duplicated, return true
                if(nums[i] == nums[j]) return true;
            }
        }
        // if not duplicated, return false
        return false;
    }
}

// 2. sorting the array and then check if any two elements are same
// time complexity is O(n log n) as it requires sorting the array (divide-and-conquer)
class Solution {
    public boolean containsDuplicate(int[] nums) {
        // sort the array
        Arrays.sort(nums);
        // iterate the array and check if following two elements are same
        for(int i = 0; i < nums.length - 1; i++) {
            if(nums[i] == nums[i +1]) return true;
        }
        // if the array is reached to the end without any duplicates, return false
        return false;
    }
}

// 3. using hashset to store elements in the array, and check if hashset contains the current element
// time complexity is O(N) as we iterate each element and check if the element is already in the set
class Solution {
    public boolean containsDuplicate(int[] nums) {
        // initialize the hashset 
        Set<Integer> set = new HashSet<>();
        // traverse each element in the array
        for(int i = 0; i < nums.length; i++) {
            // if set contains the current element, return true
            if(set.contains(nums[i])) return true;
            set.add(nums[i]);
        }
        // otherwise false
        return false;
    }
}

// 4. using the size of hashset and the length of array
// The size of a HashSet is the number of unique elements it contains
// time complexity is O(N) as we iterate each element performing constant time operation (set.add(num))
class Solution {
    public boolean containsDuplicate(int[] nums) {
    // initialize the hashset     
    Set<Integer> set = new HashSet<>();

    // add all elements in the array to hashset
    for (int num : nums) {
        set.add(num);
    }
    // check whether the size of hashset is smaller than the length of array
    // means that at least one duplicate element is in the given array
    return set.size() < nums.length;
    }
}