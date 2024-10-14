class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # 각 문자의 빈도를 저장하는 딕셔너리
        maxf = 0  # 현재 윈도우에서 가장 빈도가 높은 문자 수
        l = 0  # 슬라이딩 윈도우의 왼쪽 포인터
        res = 0  # 결과 값 (가장 긴 부분 문자열 길이)

        # 오른쪽 포인터로 문자열을 순회
        for r in range(len(s)):
            # 현재 문자의 빈도를 증가시킴
            count[s[r]] = count.get(s[r], 0) + 1
            # 가장 많이 등장한 문자의 빈도를 갱신
            maxf = max(maxf, count[s[r]])

            # (현재 윈도우 크기) - (가장 빈도 높은 문자 수) > k 이면 왼쪽 포인터 이동
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1  # 왼쪽 포인터가 가리키는 문자의 빈도 감소
                l += 1  # 왼쪽 포인터 이동

            # 최대 길이 갱신
            res = max(res, r - l + 1)

        return res  # 결과 반환