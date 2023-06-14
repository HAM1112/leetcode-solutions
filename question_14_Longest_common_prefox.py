class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longp = strs[0]

        for i in range(len(strs)):
            prefix = ""
            j=0
            current = strs[i]
            while j < len(longp) and j < len(current) and current[j] == longp[j]:
                prefix += current[j]
                j += 1
            longp = prefix
        return longp