

const mergesortedArrays = (arr1 = [] , arr2 = []) => {
   let result = []

   while(arr1.length && arr2.length) {
      const next = (arr1[0] < arr2[0] ) ? arr1.shift() : arr2.shift();
      result.push(next)
   }

   if(arr1.length) {
      result = result.concat(arr1)
   } else if(arr2.length) {
      result = result.concat(arr2)
   }t
}