class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(candidates, target, index, path, res):
            if target < 0: return
            if target == 0:
                res.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(candidates, target-candidates[i], i, path+[candidates[i]], res)

        dfs(candidates, target, 0, [], res)
        return res
