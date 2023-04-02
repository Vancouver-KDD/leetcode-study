
 function numDecodings(s) {
    if (s == null || s.length === 0) return 0;
    if (s[0] === '0') return 0;
  
    const arr = new Array(s.length + 1).fill(0);
  
    arr[0] = 1;
    arr[1] = 1;
  
    for (let i = 2; i <= s.length; i++) {
      const a = Number(s.slice(i - 1, i));  // last one digit
      if (a >= 1 && a <= 9) {
        arr[i] += arr[i - 1];
      }
  
      const b = Number(s.slice(i - 2, i));  // last two digits
      if (b >= 10 && b <= 26) {
        arr[i] += arr[i - 2];
      }
    }
  
    return arr[s.length];
  }