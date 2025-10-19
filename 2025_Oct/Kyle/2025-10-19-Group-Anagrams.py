from collections import defaultdict

# O(MNlogN)
class BruteForceSolution(object):
    def groupAnagrams(self, strs):
        n = len(strs)
        sorted_forms = ["".join(sorted(s)) for s in strs]
        visited = [False] * n
        result = []

        for i in range(n):
            if visited[i]:
                continue

            group = [strs[i]]
            visited[i] = True

            for j in range(i + 1, n):
                if not visited[j] and sorted_forms[i] == sorted_forms[j]:
                    group.append(strs[j])
                    visited[j] = True
            result.append(group)

        return result

# O(MN)
class OptimalSolution(object):
    def groupAnagrams(self, strs):
        output = defaultdict(list)
        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord("a")] += 1
            output[tuple(count)].append(word)

        return output.values()
