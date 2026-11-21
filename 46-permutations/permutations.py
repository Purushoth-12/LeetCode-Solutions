class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        used = set()

        def backtrack():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in nums:
                if num in used:
                    continue
                used.add(num)
                path.append(num)
                backtrack()
                path.pop()
                used.remove(num)

        backtrack()
        return res