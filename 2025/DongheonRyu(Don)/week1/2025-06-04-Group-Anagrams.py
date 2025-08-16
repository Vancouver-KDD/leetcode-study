

def groupAnagrams(strs):
    result = {}
    for word in strs:
        key = ''.join(sorted(word))
        if key in result:
            result[key].append(word)
        else:
            result[key] = [word]
    return list(result.values())



  
def arrAnargram2(strs):
    map = {}
    
    for i in strs:
        key = "".join(sorted(i)) 
            
        if key not in map:
            map[key] = []
        map[key].append(i) 
              
    return list(map.values())
        
      
          
          
      
          
      
              
              
              
              
              
              
  
  



