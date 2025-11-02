class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dic = {}
        # key: hashValue , value : list

        for s in strs:
            hashValue = self.getHashValue(s)
            if not hashValue in dic:
                dic[hashValue] = []
            dic[hashValue].append(s)

        result = []
        for key in dic:
            result.append(dic[key])
        return result

    def getHashValue(self, word):
        return hash(''.join(sorted(word)))
