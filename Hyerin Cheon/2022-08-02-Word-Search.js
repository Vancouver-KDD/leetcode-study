function exist(board, word){
  for(let i = 0; i < board.length; i++){
    for(let j = 0; j < board[0].length; j++){
      if(board[i][j] === word[0] && check(i, j, 0)) return true;
    }
  }
  return false;

  function check(r, c, i){
    // out of boundary
    if(r < 0 || c < 0 || r >= board.length || c >= board[0].length) return false;
    // wrong character
    if(board[r][c] != word[i]) return false;
    // got to the end means found correct path
    if(i === word.length - 1) return true;
    //mark out so we don't revist, don't go back and forth
    board[r][c] = '#';

    // try all directions
    if(check(r+1, c, i+1) || check(r-1, c, i+1) || check(r, c+1, i+1) || check(r, c-1, i+1)){
      return true;
    }
    // reset our board
    board[r][c] = word[i];
  }
}