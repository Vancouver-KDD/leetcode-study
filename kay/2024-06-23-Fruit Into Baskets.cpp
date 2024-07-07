#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int left = 0;
        int maxNum = 1;
        int right = left + 1;
        int curNum = 1;
        unordered_map<int, int> basketTypeForMap;
        basketTypeForMap[fruits[left]]++;
        while (right < fruits.size()) {
            basketTypeForMap[fruits[right]]++;
            while (basketTypeForMap.size() > 2) {
                basketTypeForMap[fruits[left]]--;
                if (basketTypeForMap[fruits[left]] == 0)
                    basketTypeForMap.erase(fruits[left]);
                left += 1;
            }
            maxNum = max(maxNum, right - left + 1);
            right += 1;
        }
        return maxNum;
    }
};

/*
Problem Understanding and Approach
English:
The problem is to find the longest subarray containing at most two distinct types of fruits. We need to efficiently keep track of the fruit types in the current subarray and their counts.

Korean:
이 문제는 최대 두 종류의 과일을 포함하는 가장 긴 서브어레이를 찾는 것입니다. 현재 서브어레이의 과일 종류와 그 개수를 효율적으로 추적해야 합니다.

Data Structures Used
English:

unordered_map<int, int> fruitCount: To count the occurrences of each fruit type in the current subarray.
int left: To keep track of the left boundary of the sliding window.
int maxNum: To store the maximum length of the subarray with at most two distinct fruit types.
int right: To iterate through the array.
int curNum: To keep track of the current number of fruits in the window (not needed after refactoring).
Korean:

unordered_map<int, int> fruitCount: 현재 서브어레이의 각 과일 종류의 발생 빈도를 계산하기 위해 사용합니다.
int left: 슬라이딩 윈도우의 왼쪽 경계를 추적하기 위해 사용합니다.
int maxNum: 최대 두 종류의 과일을 포함하는 서브어레이의 최대 길이를 저장하기 위해 사용합니다.
int right: 배열을 순회하기 위해 사용합니다.
int curNum: 윈도우 안의 현재 과일 개수를 추적하기 위해 사용합니다 (리팩토링 후 불필요함).
Algorithm Steps
English:

Initialize variables left, maxNum, and fruitCount.
Traverse the array with the right pointer.
For each element at right, add it to the hash map and update the count.
If the window contains more than two types of fruits, adjust the window by removing the leftmost fruit and moving the left pointer.
Update maxNum with the current window size if it's larger.
Return maxNum after traversing the array.
Korean:

변수 left, maxNum, fruitCount를 초기화합니다.
right 포인터로 배열을 순회합니다.
right에 있는 각 요소를 해시 맵에 추가하고 개수를 업데이트합니다.
윈도우가 두 종류 이상의 과일을 포함하면, 가장 왼쪽 과일을 제거하고 left 포인터를 이동시켜 윈도우를 조정합니다.
현재 윈도우 크기가 더 크면 maxNum을 업데이트합니다.
배열을 다 순회한 후 maxNum을 반환합니다.
Code Explanation Line by Line
Code:

cpp
코드 복사
class FruitBasket {
public:
    int totalFruit(vector<int>& fruits) {
        int left = 0; // Initialize the left pointer of the sliding window
        int maxNum = 1; // Initialize maxNum to store the maximum length of the subarray with at most two distinct fruit types
        int right = 0; // Initialize the right pointer of the sliding window
        unordered_map<int, int> fruitCount; // Initialize a hash map to count occurrences of each fruit type in the current subarray

        while (right < fruits.size()) { // Traverse the array with the right pointer
            fruitCount[fruits[right]]++; // Increment the count of the current fruit in the hash map

            while (fruitCount.size() > 2) { // If the window contains more than two types of fruits
                fruitCount[fruits[left]]--; // Decrement the count of the leftmost fruit
                if (fruitCount[fruits[left]] == 0) { // If the count becomes zero, remove it from the hash map
                    fruitCount.erase(fruits[left]);
                }
                left++; // Move the left pointer to the right
            }

            maxNum = max(maxNum, right - left + 1); // Update maxNum with the current window size if it's larger
            right++; // Move the right pointer to the right
        }

        return maxNum; // Return the maximum length of the subarray with at most two distinct fruit types
    }
};
Line-by-line Explanation:

class FruitBasket {

English: Define the FruitBasket class.
Korean: FruitBasket 클래스를 정의합니다.
public:

English: Define the public access specifier.
Korean: public 접근 지정자를 정의합니다.
int totalFruit(vector<int>& fruits) {

English: Define the totalFruit function that takes a vector of integers representing fruit types and returns an integer.
Korean: 과일 종류를 나타내는 정수 벡터를 입력으로 받아 정수를 반환하는 totalFruit 함수를 정의합니다.
int left = 0;

English: Initialize the left pointer of the sliding window.
Korean: 슬라이딩 윈도우의 왼쪽 포인터를 초기화합니다.
int maxNum = 1;

English: Initialize maxNum to store the maximum length of the subarray with at most two distinct fruit types.
Korean: 최대 두 종류의 과일을 포함하는 서브어레이의 최대 길이를 저장하기 위해 maxNum을 초기화합니다.
int right = 0;

English: Initialize the right pointer of the sliding window.
Korean: 슬라이딩 윈도우의 오른쪽 포인터를 초기화합니다.
unordered_map<int, int> fruitCount;

English: Initialize a hash map to count occurrences of each fruit type in the current subarray.
Korean: 현재 서브어레이의 각 과일 종류의 발생 빈도를 계산하기 위해 해시 맵을 초기화합니다.
while (right < fruits.size()) {

English: Traverse the array with the right pointer.
Korean: right 포인터로 배열을 순회합니다.
fruitCount[fruits[right]]++;

English: Increment the count of the current fruit in the hash map.
Korean: 해시 맵에서 현재 과일의 개수를 증가시킵니다.
while (fruitCount.size() > 2) {

English: If the window contains more than two types of fruits.
Korean: 윈도우가 두 종류 이상의 과일을 포함하면.
fruitCount[fruits[left]]--;

English: Decrement the count of the leftmost fruit.
Korean: 가장 왼쪽 과일의 개수를 감소시킵니다.
if (fruitCount[fruits[left]] == 0) {

English: If the count becomes zero, remove it from the hash map.
Korean: 개수가 0이 되면 해시 맵에서 제거합니다.
fruitCount.erase(fruits[left]);

English: Remove the element from the hash map.
Korean: 요소를 해시 맵에서 제거합니다.
left++;

English: Move the left pointer to the right.
Korean: 왼쪽 포인터를 오른쪽으로 이동시킵니다.
}

English: Close the while (fruitCount.size() > 2) block.
Korean: while (fruitCount.size() > 2) 블록을 닫습니다.
maxNum = max(maxNum, right - left + 1);

English: Update maxNum with the current window size if it's larger.
Korean: 현재 윈도우 크기가 더 크면 maxNum을 업데이트합니다.
right++;

English: Move the right pointer to the right.
Korean: 오른쪽 포인터를 오른쪽으로 이동시킵니다.
}

English: Close the while (right < fruits.size()) block.
Korean: while (right < fruits.size()) 블록을 닫습니다.
return maxNum;

English: Return the maximum length of the subarray with at most two distinct fruit types.
Korean: 최대 두 종류의 과일을 포함하는 서브어레이의 최대 길이를 반환합니다.
}

English: Close the totalFruit function.
Korean: totalFruit 함수를 닫습니다.
};

English: Close the FruitBasket class.
Korean: FruitBasket 클래스를 닫습니다.
Complexity Analysis
Time Complexity (T(c)):

English:
The time complexity is O(N) because each element is processed at most twice - once by the right pointer and at most once by the left pointer.

Korean:
시간 복잡도는 O(N)입니다. 각 요소는 오른쪽 포인터에 의해 한 번, 왼쪽 포인터에 의해 최대 한 번 처리되기 때문입니다.

Space Complexity (S(c)):

English:
The space complexity is O(1) because the hash map will contain at most 3 keys at any given time (since there are only 2 types of fruits allowed and the extra one is for the condition check).

Korean:
공간 복잡도는 O(1)입니다. 해시 맵은 최대 3개의 키를 포함할 수 있기 때문입니다 (최대 2종류의 과일만 허용되고, 조건 확인을 위해 추가된 하나입니다).*/