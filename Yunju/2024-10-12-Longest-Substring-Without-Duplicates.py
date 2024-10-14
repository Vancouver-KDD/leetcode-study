class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet: #현재 오른쪽 포인터 r이 가리키는 문자 s[r]**이 charSet에 있는지 확인하고 있으면 반복
                charSet.remove(s[l]) #왼쪽 포인터 l이 가리키는 문자를 지움
                l += 1 #l은 다음 으로 이동
            charSet.add(s[r]) #s[r]이 charSet에 없으면 s[r]을 추가
            res = max(res, r - l + 1) 
            #res는 지금까지 나왔던 res의 max값과 오른쪽 포인터에서 왼쪽 포인터를 빼고 1을 더한값(문자열의 길이) 중 최대값을 구함.
            #+1을 더하는 이유는 인덱스는 0부터 시작하니까
        return res