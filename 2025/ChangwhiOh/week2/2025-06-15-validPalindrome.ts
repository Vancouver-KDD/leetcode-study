function isPalindrome(s: string): boolean {
        const arr = s.toLowerCase().replace(/[^0-9a-z]/g, "").split(""); //dafsdcqjwcdkc
  
  	let p1 = 0;
  	let p2 = arr.length - 1
    
    while(p1<p2){
      if (arr[p1] !== arr[p2]) return false;
      p1++;
      p2--;
    }
  	
  return true;
    
};