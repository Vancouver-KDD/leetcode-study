
var exist = function(board, word) {
    if(board.length === 0) return false;

   const h = board.length;
   const w = board[0].length;
   const dirs = [[-1, 0], [0,1], [1,0], [0,-1]];

   const go = (x,y,k) => {
       if(board[x][y] != word[k]) return false;
       if(k === word.length -1) return true;

       board[x][y] = '*';
       for(const [dx, dy] of dirs) {
           const i = x+dx;
           const j = y+dy;
           if(i >= 0 && i < h && j >=0 && j<w){
               if(go(i,j, k+1)) return true;
           }
       }

       board[x][y] = word[k];
       return false;
   };

   for(let i=0; i<h; i++) {
       for(let j=0; j<w; j++) {
           if(go(i,j,0)) return true;
       }
   }
   return false;
};