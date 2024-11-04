## Approach
- First create a map as the digit - letter combination in the dial pad.
- Rather than a brute force nested interations for each digit, use backtracking technique recursively.

### Complexity
- Time complexity - O(n * 4^n) - n is the number of the digit
- Space complexity - O(4^n)

### Solution
```
# @param {String} digits
# @return {String[]}

def letter_combinations(digits)
    # First create a map
    chars = "abcdefghijklmnopqrstuvwxyz".split ""

    @map = Hash.new()
    i = 0
    number = 2

    while number <= 9 do
        if number == 7 || number == 9
             @map[number.to_s] = chars[i..i+3]
            i += 4 
        else
            @map[number.to_s] = chars[i..i+2]
            i += 3
        end
        number += 1
    end
    #@map = {"2"=>["a", "b", "c"], "3"=>["d", "e", "f"], "4"=>["g", "h", "i"], "5"=>["j", "k", "l"], "6"=>["m", "n", "o"], "7"=>["p", "q", "r", "s"], "8"=>["t", "u", "v"], "9"=>["w", "x", "y", "z"]}

    
    # Now process the given digit
    @res = []

    if digits
        backtrack(0, "", digits)
    end

    return [] if @res == [""]
    @res
end

def backtrack(i, cur_str, digits)
    if cur_str.size == digits.size
        @res << cur_str
        return
    end

    for c in @map[digits[i]]
        backtrack(i + 1, cur_str + c, digits)
    end
end
```
