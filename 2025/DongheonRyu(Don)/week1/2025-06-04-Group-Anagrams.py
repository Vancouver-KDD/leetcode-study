
def groupAnagrams(strs):
    result = {}
    for word in strs:
        key = ''.join(sorted(word))
        if key in result:
            result[key].append(word)
        else:
            result[key] = [word]
    return list(result.values())