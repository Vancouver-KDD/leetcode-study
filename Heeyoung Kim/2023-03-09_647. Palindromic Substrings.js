const countSubstings = (s) => {
    let count=0;

    const bubbleFromCenter = (left, right) => {
        while(left >= 0 && right < s.length && s[left] === s[right]) {
            count++; left--; right++;
        }
    };

    for(let i=0; i<s.length; i++) {
        bubbleFromCenter(i,i);
        bubbleFromCenter(i,i+1);
    }

    return count;
} 