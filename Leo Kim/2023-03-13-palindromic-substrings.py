class Solution:
	def countSubstrings(self, s: str) -> int:

		result = 0

		for i in range(len(s)):
			for j in range(i,len(s)):
				if s[i:j+1] == s[i:j+1][::-1]:
					result = result +1

		return result