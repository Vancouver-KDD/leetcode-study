const LCS = (arr) => {
  //get unique elms
  const S = new Set(arr);

  //store the result
  let max = 1;

  // iterate array elements
  for (let e of arr) {

    // if the current element begins a new seq
    if (!S.has(e - 1)) {

      // tracks the length of subsequence
      let len = 1;

      // count all the elements of the subsequence
      // e+1, e+2,...
      while (S.has(e + len)) {
        len++;
      }

      // get the max subsequence
      max = Math.max(max, len);
    }
  }

  return max;
}
