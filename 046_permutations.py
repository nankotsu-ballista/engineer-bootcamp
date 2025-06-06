class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, remain):
            if not remain:
                res.append(path)
                return

            for i in range(len(remain)):
                backtrack(
                    path + [remain[i]],
                    remain[:i] + remain[i+1:]
                )
        
        backtrack([], nums)
        return res
