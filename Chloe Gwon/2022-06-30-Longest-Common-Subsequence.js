var longestCommonSubsequence = function(text1, text2) {
    let prevRow = Array(text2.length + 1).fill(0);
    for (var i=1; i<=text1.length; i++){
        const curRow = Array(text2.length+1).fill(0);
        for (var j=1; j<=text2.length; j++){
            if (text1[i-1] === text2[j-1]){
                curRow[j] = 1 + prevRow[j-1];
            }else{
                curRow[j] = Math.max(curRow[j-1], prevRow[j]);
            }
        }
        prevRow = curRow;
    }
    return prevRow[text2.length];
};
