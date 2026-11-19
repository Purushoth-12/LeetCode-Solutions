class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res: list[list[int]] = []
        path: list[int] = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                val = candidates[i]
                if val > remaining:
                    break

                path.append(val)
                backtrack(i + 1, remaining - val)
                path.pop()

        backtrack(0, target)
        return res