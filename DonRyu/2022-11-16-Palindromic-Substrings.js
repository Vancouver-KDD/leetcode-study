var longestPalindrome = function(s) {
    let currentLongest = [0, 1];

    for (let i=1; i< s.length; i++){
        const odd = expandAroundCenter(s, i-1, i+1); // treating the given letter as a center and checking its surrounding letters
        const even = expandAroundCenter(s, i-1, i); // checking if the  center is between the given letter and the previous letter
        const longest = odd[1] - odd[0] > even[1] - even[0] ? odd : even; // choosing the longest palindrome between odd and even
        currentLongest = currentLongest[1] - currentLongest[0] > longest [1] - longest[0] ?  currentLongest : longest // comparing the longest to the current longest palindrome and updating current longest accordingly
    }
    return s.slice(currentLongest[0], currentLongest[1]);
};

function expandAroundCenter(s, leftIdx, rightIdx){
    while (leftIdx >= 0 && rightIdx < s.length){
        if(s[leftIdx] !== s[rightIdx]) break;
        leftIdx--;
        rightIdx++;
    }
    return[leftIdx + 1, rightIdx]
}
