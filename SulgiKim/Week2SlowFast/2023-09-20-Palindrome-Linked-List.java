/* https://leetcode.com/problems/palindrome-linked-list/description/
 * 
 * ## Description 
 * Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
 * 
 */

// 1. Easy Solution with Two pointers 
// Create an array so that we can use the indices to compare from the both ends, 
//                          instead of a singly linked list, which we can only access elements in one direction. 
// Space Complexity: O(n)

class Solution {
    public boolean isPalindrome(ListNode head) {
        //Create an array and store the head's values 
        List<Integer> nums = new ArrayList<>(); 
        while (head != null) {
            nums.add(head.val); 
            head = head.next;
        }
        
        //Set the two pointers at both ends of nums 
        int left = 0, right = nums.size() - 1; 
        
        //Check every elements until left and right pointers meet 
        while (left <= right) {
            //Compare from the both ends and if it's not  the same, it will return false 
            if(nums.get(left) != nums.get(right)) {
                return false;
            }
            //Converge the pointers 
            left++; 
            right--; 
        }
        return true;
    }
}


// 2. Optimized Solution 
// To accomplish O(1) space complexity, it requires us to access from the both ends of node rather than storing its value in a new array. 
// By using slow and fast pointers & Floyd's cycle detection algorithm, we could place the pointer at the middle of linked list.
// Then we could reverse the back half of the linked list and check if it's palindrome from the both ends using no extra space! 

class Solution {
    public boolean isPalindrome(ListNode head) {
        // Initialize the pointers 
        ListNode slow = head, fast = head, prev, temp; 
        
        //Place slow pointer at the middle
        while (fast != null && fast.next != null) { //Need to check for both cases for odd & even number of elements in head.
            slow = slow.next; 
            fast = fast.next.next; // move twice faster than slow
        }
        
        //Set the pointers for reversal 
        prev = slow;
        slow = slow.next;
        prev.next = null; // to avoid an endless loop 

        //Reversal process
        while (slow != null){ 
            temp = slow.next; 
            slow.next = prev; 
            prev = slow; 
            slow = temp; 
        }

        //Place the pointers at the both end nodes
        fast = head; 
        slow = prev; 

        while(slow != null) {
            //Compare from the both ends and if it's not  the same, it will return false 
            if(fast.val != slow.val){
                return false;
            }

            //Converge the pointers
            fast = fast.next;
            slow= slow.next;
        }

        return true; 
    }

}