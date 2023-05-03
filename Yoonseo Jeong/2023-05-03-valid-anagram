var isAnagram = function(s, t) {
    // check if parameters are valid
    if (!s || !t || s.length < 1 || t.length < 1 || s.length != t.length) {
        return false
    }

    // need to check all letters of each string matches the same
    // sort out both given string in alphabetical order and compare them
    return [...s].sort().join("") === [...t].sort().join("") ? true : false

    // simple solution using JavaScript Array methods
    // complexity
    // time: O(n + m) or O(n log n) - cause Array sort method's sorting method can differ
    // space: O(1)
};

var isAnagram2 = function(s, t) {
    // check if parameters are valid
    if (!s || !t || s.length < 1 || t.length < 1 || s.length != t.length) {
        return false
    }

    // to do it without sorting
    // check what charater they have and numbers of them and compare
    let alphList = {}
    for (let item of s) {
        if (!alphList[item]) {
       		alphList[item] = 0;
        }
        alphList[item]++;
    }
    for (let item of t) {
        if(alphList[item] == undefined) {
        	return false;
        }
        alphList[item]--;
    }
    for (let item in alphList) {
        if (alphList[item] !== 0) {
            return false
        }
    }
    return true

    // complexity
    // time: O(n + m)
    // space: O(n)
}