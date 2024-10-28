## Approach
- Initialize a hash structure that each key is also a hash (key - timestamp, value - value)
- ex) {"foo" => {"1" => "bar", "4" => "bar2"}, "foo2" => {"1" => "bar3"}}
- For get function, make a list of timestamps and values of the given key. Do binary search with the timestamps list

### Complexity
- Time complexity - O(log(n))
- Space complexity - O(n)

### Solution
```
class TimeMap
    attr_reader :hash

    def initialize()
        @hash = Hash.new({})
    end


=begin
    :type key: String
    :type value: String
    :type timestamp: Integer
    :rtype: Void
=end
    def set(key, value, timestamp)
        if hash.has_key?(key)
            hash[key][timestamp] = value
        else
            hash[key] = {timestamp => value}
        end
    end

=begin
    :type key: String
    :type timestamp: Integer
    :rtype: String
=end
    def get(key, timestamp)
        return '' if !hash.has_key?(key)

        timestamps = hash[key].keys
        values = hash[key].values
        return '' if timestamps.empty? || timestamp < timestamps[0] 
        
        left = 0
        right = timestamps.length - 1
        while left <= right
            mid = (left + right) / 2
            if timestamps[mid] == timestamp
                return values[mid]
            elsif timestamps[mid] < timestamp
                left = mid + 1
            else
                right = mid - 1
            end
        end

        return values[right]
    end
end
```
