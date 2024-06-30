class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) { // O(N)
        long long maxSum = 0;
        long long curSum = 0;
        int left = 0, right = 0;
        unordered_map<int, int> elementCount;
        while (right < k && right < nums.size()) {
            elementCount[nums[right]]++;
            curSum += nums[right++];
        }
        if (elementCount.size() == k)
            maxSum = curSum;
        while (right < nums.size()) {
            elementCount[nums[left]]--;
            if (elementCount[nums[left]] == 0)
                elementCount.erase(nums[left]);
            elementCount[nums[right]]++;
            curSum = curSum - nums[left] + nums[right];
            if (elementCount.size() == k)
                maxSum = max(maxSum, curSum);
            left++;
            right++;
        }
        return maxSum;
    }
};
/*


Problem Understanding and Approach
English:
The problem is to find the maximum sum of a subarray of length k where all elements in the subarray are unique. This requires us to efficiently keep track of the elements in the current subarray, their counts, and the sum of the subarray.

Korean:
이 문제는 길이가 k인 서브어레이의 합 중에서 모든 요소가 고유한 경우의 최대 합을 찾는 것입니다. 이를 위해 현재 서브어레이의 요소, 그들의 개수, 서브어레이의 합을 효율적으로 추적해야 합니다.

English:
To solve this problem, we can use a sliding window approach combined with a hash map. The sliding window will help in maintaining a subarray of size k, and the hash map will keep track of the count of each element within the window.

Korean:
이 문제를 해결하기 위해 슬라이딩 윈도우 접근법과 해시 맵을 결합하여 사용할 수 있습니다. 슬라이딩 윈도우는 길이가 k인 서브어레이를 유지하는 데 도움이 되며, 해시 맵은 윈도우 내 각 요소의 개수를 추적하는 데 사용됩니다.

Data Structures Used
English:

unordered_map<int, int> elementCount: To count the occurrences of elements in the current subarray.
long long currentSum: To keep track of the sum of the current subarray.
long long maxSum: To store the maximum sum of a subarray with unique elements of size k.
Korean:

unordered_map<int, int> elementCount: 현재 서브어레이의 요소 발생 빈도를 계산하기 위해 사용합니다.
long long currentSum: 현재 서브어레이의 합을 추적하기 위해 사용합니다.
long long maxSum: 길이가 k인 고유한 요소를 가진 서브어레이의 최대 합을 저장하기 위해 사용합니다.
Algorithm Steps
English:

Initialize variables maxSum, currentSum, and left.
Traverse the array with a right pointer.
For each element at right, add it to the hash map and update the current sum.
If the window size exceeds k, adjust the window by removing the leftmost element and moving the left pointer.
If the window size is k and all elements are unique, update maxSum.
Return maxSum after traversing the array.
Korean:

변수 maxSum, currentSum, left를 초기화합니다.
right 포인터로 배열을 순회합니다.
right에 있는 각 요소를 해시 맵에 추가하고 현재 합을 업데이트합니다.
윈도우 크기가 k를 초과하면, 가장 왼쪽 요소를 제거하고 left 포인터를 이동시켜 윈도우를 조정합니다.
윈도우 크기가 k이고 모든 요소가 고유한 경우 maxSum을 업데이트합니다.
배열을 다 순회한 후 maxSum을 반환합니다.


Code Explanation Line by Line

Code:

class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        long long maxSum = 0; // Initialize maxSum to store the maximum sum of a subarray with unique elements of size k
        long long currentSum = 0; // Initialize currentSum to keep track of the current subarray's sum
        int left = 0; // Initialize the left pointer of the sliding window
        unordered_map<int, int> elementCount; // Initialize a hash map to count occurrences of elements in the current subarray

        for (int right = 0; right < nums.size(); ++right) { // Traverse the array with the right pointer
            elementCount[nums[right]]++; // Increment the count of the current element in the hash map
            currentSum += nums[right]; // Add the current element to the current sum

            if (right - left + 1 > k) { // If the window size exceeds k
                elementCount[nums[left]]--; // Decrement the count of the leftmost element
                if (elementCount[nums[left]] == 0) { // If the count becomes zero, remove it from the hash map
                    elementCount.erase(nums[left]);
                }
                currentSum -= nums[left]; // Subtract the leftmost element from the current sum
                left++; // Move the left pointer to the right
            }

            if (right - left + 1 == k && elementCount.size() == k) { // If the window size is k and all elements are unique
                maxSum = max(maxSum, currentSum); // Update maxSum with the current sum if it is larger
            }
        }

        return maxSum; // Return the maximum sum of a subarray with unique elements of size k
    }
};


Line-by-line Explanation:

class Solution {

English: Define the Solution class.
Korean: Solution 클래스를 정의합니다.
public:

English: Define the public access specifier.
Korean: public 접근 지정자를 정의합니다.
long long maximumSubarraySum(vector<int>& nums, int k) {

English: Define the maximumSubarraySum function that takes a vector of integers and an integer k as input and returns a long long integer.
Korean: 정수 벡터와 정수 k를 입력으로 받아 long long 정수를 반환하는 maximumSubarraySum 함수를 정의합니다.
long long maxSum = 0;

English: Initialize maxSum to store the maximum sum of a subarray with unique elements of size k.
Korean: 길이가 k인 고유한 요소를 가진 서브어레이의 최대 합을 저장하기 위해 maxSum을 초기화합니다.
long long currentSum = 0;

English: Initialize currentSum to keep track of the current subarray's sum.
Korean: 현재 서브어레이의 합을 추적하기 위해 currentSum을 초기화합니다.
int left = 0;

English: Initialize the left pointer of the sliding window.
Korean: 슬라이딩 윈도우의 왼쪽 포인터를 초기화합니다.
unordered_map<int, int> elementCount;

English: Initialize a hash map to count occurrences of elements in the current subarray.
Korean: 현재 서브어레이의 요소 발생 빈도를 계산하기 위해 해시 맵을 초기화합니다.
for (int right = 0; right < nums.size(); ++right) {

English: Traverse the array with the right pointer.
Korean: right 포인터로 배열을 순회합니다.
elementCount[nums[right]]++;

English: Increment the count of the current element in the hash map.
Korean: 해시 맵에서 현재 요소의 개수를 증가시킵니다.
currentSum += nums[right];

English: Add the current element to the current sum.
Korean: 현재 요소를 현재 합에 더합니다.
if (right - left + 1 > k) {

English: If the window size exceeds k.
Korean: 윈도우 크기가 k를 초과하면.
elementCount[nums[left]]--;

English: Decrement the count of the leftmost element.
Korean: 가장 왼쪽 요소의 개수를 감소시킵니다.
if (elementCount[nums[left]] == 0) {

English: If the count becomes zero, remove it from the hash map.
Korean: 개수가 0이 되면 해시 맵에서 제거합니다.
elementCount.erase(nums[left]);

English: Remove the element from the hash map.
Korean: 요소를 해시 맵에서 제거합니다.
currentSum -= nums[left];

English: Subtract the leftmost element from the current sum.
Korean: 현재 합에서 가장 왼쪽 요소를 뺍니다.
left++;

English: Move the left pointer to the right.
Korean: 왼쪽 포인터를 오른쪽으로 이동시킵니다.
if (right - left + 1 == k && elementCount.size() == k) {

English: If the window size is k and all elements are unique.
Korean: 윈도우 크기가 k이고 모든 요소가 고유한 경우.
maxSum = max(maxSum, currentSum);

English: Update maxSum with the current sum if it is larger.
Korean: 현재 합이 더 크면 maxSum을 업데이트합니다.
}

English: Close the if and for blocks.
Korean: if와 for 블록을 닫습니다.
return maxSum;

English: Return the maximum sum of a subarray with unique elements of size k.
Korean: 길이가 k인 고유한 요소를 가진 서브어레이의 최대 합을 반환합니다.
}

English: Close the maximumSubarraySum function.
Korean: maximumSubarraySum 함수를 닫습니다.
};

English: Close the Solution class.
Korean: Solution 클래스를 닫습니다.
*/