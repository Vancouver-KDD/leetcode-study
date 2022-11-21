
var longestPalindrome = function (string) {
    let longestPalLength = 0;
    let longestPalLeft = 0;
    let longestPalRight = 0;

    var getLongestPalindrome = function (leftPosition, rightPosition) {
        // While there is space to expand, and the expanded strings match
        while (
            leftPosition >= 0 &&
            rightPosition < string.length &&
            string[leftPosition] === string[rightPosition]
        ) {
            //expand in each direction.
            leftPosition--;
            rightPosition++;
        }

        // Store the longest palindrome (if it's the longest one found so far)
        if (rightPosition - leftPosition > longestPalLength) {
            longestPalLeft = leftPosition + 1;
            longestPalRight = rightPosition - 1;
            longestPalLength = longestPalRight - longestPalLeft + 1;
        }
    };

     // Loop through the letters
    for (let i = 0; i < string.length; i++) {
        // Find the longest odd palendrome
        getLongestPalindrome(i, i + 1);

        // Find the longest even palendrome
        getLongestPalindrome(i, i);

        // Check if a longer palindrome cannot be found
        if ((string.length - i) * 2 < longestPalLength) {
            // Break out to avoid unnecessary computation
            break;
        }
    }

    return string.slice(longestPalLeft, longestPalRight + 1);
};
