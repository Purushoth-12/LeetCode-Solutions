


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = [False] * len(nums)
        result: List[List[int]] = []
        current: List[int] = []

        def backtrack() -> None:
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                current.append(nums[i])
                backtrack()
                current.pop()
                used[i] = False

        backtrack()
        return result