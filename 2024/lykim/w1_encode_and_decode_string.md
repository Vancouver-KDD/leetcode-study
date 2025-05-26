## Approach
- Set a delimiter to split each element and also add a number before the delimiter - to be clear if the delimiter is the correct one, not from the string itself
- Decode based on it.

### Complexity
- Time complexity - O(n)
- Space complexity - O(n)

### Solution
```
DELIMITER = "#"
def encode(strs)
    res = ''
    strs.each do |str|
        encoded = str.size + DELIMITER + str
        res += encoded
    end

    res
end

def decode(str)
  res = []
  i = 0
  while i < str.size do
    j = i
    while str[j] != DELIMITER do
      j += 1
    end

    length = str[i..j]
    res << str[j+1..j+1+length]
    i = j + 1 + length
  end

  res
end
```
