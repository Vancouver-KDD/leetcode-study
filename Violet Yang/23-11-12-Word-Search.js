var exist = function(board, word) {
    var len1 = board.length;
    var len2 = (board[0] || []).length;
    var len3 = word.length;
    var visited = null;
  
    if (!len1 || !len2 || !len3) return false;
  
    for (var i = 0; i < len1; i++) {
      for (var j = 0; j < len2; j++) {
        visited = Array(len1).fill(0).map(_ => Array(len2));
        if (helper(board, word, i, j, 0, visited)) return true;
      }
    }
  
    return false;
  };
  
  var helper = function (board, word, m, n, k, visited) {
    if (k === word.length) return true;
    if (m < 0 || m >= board.length) return false;
    if (n < 0 || n >= board[m].length) return false;
    if (visited[m][n]) return false;
    if (board[m][n] !== word[k]) return false;
  
    var res = false;
  
    visited[m][n] = true;
  
    res = helper(board, word, m - 1, n, k + 1, visited)
          || helper(board, word, m + 1, n, k + 1, visited)
          || helper(board, word, m, n - 1, k + 1, visited)
          || helper(board, word, m, n + 1, k + 1, visited);
  
    if (!res) visited[m][n] = false;
  
    return res;
  };
  