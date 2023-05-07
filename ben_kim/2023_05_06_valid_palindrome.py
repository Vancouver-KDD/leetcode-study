class Solution:
    def valid_palindrome(self, s: str) -> bool:
        s = s.lower()
        alphanum_list = list(filter(str.isalnum, s))
        
        l, r = 0, len(alphanum_list) - 1
        '''
        1, 2, 3
        홀수인경우 하나의 인덱스에서 만나게된다
        
        1, 2, 3, 4
        짝수인 경우 이전작업 수 l과 r의 인덱스가 바뀌게 된다
        '''
        
        while l < r:
            if not alphanum_list[l] == alphanum_list[r]:
                return False
            l += 1
            r -= 1
        
        return True