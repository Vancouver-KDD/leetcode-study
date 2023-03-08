/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
 var checkInclusion = function(s1, s2) {
    //sliding window length = s1.length;

	if (s1.length > s2.length) return false;
	let map = {}; 
	for (let i = 0; i < s1.length; i++) {
		map[s1[i]] = (map[s1[i]] || 0) + 1;
	}
	
	let left = 0, 
		right = 0, 
		requiredLength = s1.length;

	while (right < s2.length) {
		
		if (map[s2[right]] > 0) requiredLength--;
		
		map[s2[right]]--;
		right++ 

		
		if (requiredLength === 0) return true;


		if (right - left === s1.length) {
			if (map[s2[left]] >= 0) requiredLength++;
			map[s2[left]]++;
			left++
		}
	}
	return false;
};

//Time Complexity : O(n)
//Space Complexity : O(n)