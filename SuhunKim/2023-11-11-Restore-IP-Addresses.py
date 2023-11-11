class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def helper(ip, string):
            if len(string) == 0 and len(ip) == 4:
                res.append(".".join(ip))
                return
            
            temp = ""
            for i in range(len(string)):
                temp += string[i]
                if temp[0] == "0" and len(temp) > 1:
                    break
                if int(temp) >= 0 and int(temp) <= 255:
                    ip.append(temp)
                    helper(ip, string[i+1:])
                    ip.pop()
                else:
                    break
        
        helper([], s)
        
        return res