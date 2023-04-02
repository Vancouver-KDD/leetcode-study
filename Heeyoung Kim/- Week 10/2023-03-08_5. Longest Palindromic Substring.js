let longestPalindrome = (s) => {
    let maxSub = '';

    const bubbelFromCenter = (left, right) =>{
        while(left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        } 
        return s.slice(left+1, right);
    }

    for(let i=0; i<s.length; i++) {
        const sub1 = bubbelFromCenter(i,i);
        const sub2 = bubbelFromCenter(i, i+1);
        const sub = sub1.length > sub2.length ? sub1 : sub2
        if(sub.length > maxSub.length) {maxSub = sub}
    }

    return maxSub;
}