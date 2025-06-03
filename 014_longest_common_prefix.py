class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            char = shortest[i]
            for s in strs:
                if s[i] != char:
                    return shortest[:i]

        return shortest
        
