class Solution:
    def computeCharCounts(self, string: str) -> Set[Tuple[str,int]]:
        charCounts = [0] * 26
        for char in string:
            charCounts[ord(char) - ord("a")] += 1
        return tuple(charCounts)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramStrings = {}
        for string in strs:
            charCounts = self.computeCharCounts(string)
            anagramStringList = anagramStrings.get(charCounts, [])
            anagramStringList.append(string)
            anagramStrings[charCounts] = anagramStringList
        return list(anagramStrings.values())