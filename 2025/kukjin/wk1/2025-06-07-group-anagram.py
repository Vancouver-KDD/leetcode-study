
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      # rst = {}
      rst = defaultdict(list)

      for s in strs:
          ss = "".join(sorted(s))
          if ss not in rst: 
              rst[ss] = []
          rst[ss].append(s)

      return list(rst.values())