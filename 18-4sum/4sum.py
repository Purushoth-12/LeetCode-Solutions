class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 3):
            # Skip duplicate elements for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Early pruning: if smallest possible sum is too large, break
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # Early pruning: if largest possible sum is too small, continue
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicate elements for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # Early pruning for second loop
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                    
                left, right = j + 1, n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if s == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for the third number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the fourth number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
                        
        return res