var isAnagram = function (s, t) {
	if (s.length != t.length) return false;
	const hashTable = {};

	for (let i = 0; i < s.length; i++) {
		if (!hashTable[s[i]]) {
			hashTable[s[i]] = 0;
		}
		hashTable[s[i]]++;
	}

	for (let j = 0; j < t.length; j++) {
		if (!hashTable[t[j]]) {
			return false;
		}
		hashTable[s[j]]--;
	}

	return true;
};
