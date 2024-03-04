class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if (num - 1) not in num_set:
                current_streak = 1
                while (num + current_streak) in num_set:
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
''' explain 

This is about:
finding the longest ascending order sequence; increased by 1 for each

인덱스 0에 있는 숫자 부터 시작하여서, 그 숫자보다 1 작은 수가 수열에 있는지 확인한다 
- how to check? 
- the time complexity for "IN-SET" operation will be O(N)
이유:
- 이유는 커런트 넘버가 어센딩 컨세큐티브 시퀀스의 시작 넘버가 될 수 있는지 아는지 확인하기 위함.
아니면 다른 넘버를 선택한다.
예를 들어서, 우리는 1,2,3,4를 찾고 싶지 3,4인 부분 수열을 찾고 싶은 것이 아님. 

스타팅 넘버가 될 만한 걸 찾았으면, 1씩 늘려가면서 각 숫자가 주어신 인풋 어레이에 있는지 확인한다.
있으면 킵 고잉, 없으면 와일 룹 이스케이프 해서 여태까지의 맥시멈 넘버와 비교한다. 



## Explanation of Longest Consecutive Sequence Algorithm

To find the length of the longest consecutive sequence in a given list of integers. 
Consecutive means differences between number is "1".
Here's a concise explanation of how it works:

1. **Initialization**: 
   - Initialize the variable `longest_streak` to keep track of the longest consecutive sequence found so far. 
   - Create a set `num_set` from the input list `nums` to allow for efficient lookup of numbers. 
      ---> since IN operation for set is O(N)

2. **Iteration**: 
   - Iterate through each number in the set `num_set`.

3. **Checking Sequence Start**: 
   - For each number, check if its predecessor (i.e., `num - 1`) exists in the set `num_set`. 
   - If not found, it implies that the current number can be the start of a consecutive sequence.
     ---> We don't wanna find "3,4,5"(partial sequence) we want to find "1,2,3,4,5"(FULL sequence).

4. **Exploring Consecutive Sequence**: 
   - If the current number can potentially start a sequence, a while loop is initiated. 
   - Initialize `current_streak` to 1 and increment it as long as `num + current_streak` exists in `num_set`, indicating consecutive numbers.

5. **Updating Longest Streak**: 
   - After exploring the consecutive sequence, 
   update `longest_streak` with the maximum value between the current streak and the longest streak found so far.

'''