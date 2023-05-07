class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        # brute force t.replace(tele, "",1) replace with count
        # for sele in s:
        #     for tele in t:
        #         if sele == tele:
        #             t = t.replace(tele, "",1)
        #             break
        
        # if len(t)==0:
        #     return True
        # else:
        #     return False

        # using sort
        # newS = sorted(s)
        # newt = sorted(t)

        # for i in range(0, len(s)):
        #     if newS[i] == newt[i]:
        #         continue
        #     else:
        #         return False

        # return True

        # using dictionary checking ele in t_dic first

        # s_dic = {}
        # t_dic = {}

        # for ele in s:
        #     if ele in s_dic:
        #         s_dic[ele] += 1
        #     else:
        #         s_dic[ele] = 1

        # for ele in t:
        #     if ele in t_dic:
        #         t_dic[ele] += 1
        #     else:
        #         t_dic[ele] = 1


        # for ele in s_dic.keys():
            
        #     if ele in t_dic and s_dic[ele] == t_dic[ele]:
        #         continue
        #     else:
        #         return False

        # return True

        # using Counter
        #The Counter class is one of the classes provided by Python's collections module, 
        #and it is used to count the occurrences of elements in a sequence such as strings,
        # lists, tuples, and dictionarie

        from collections import Counter

        s_dic = Counter(s)
        t_dic = Counter(t)

        for ele in s_dic.keys():
            
            if ele in t_dic and s_dic[ele] == t_dic[ele]:
                continue
            else:
                return False
        return True


        

