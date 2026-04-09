class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        total = 0
        res = []
        nums.sort()
        for j in range(len(nums)- 2):
            l = j + 1
            r = len(nums) - 1
            if j > 0 and nums[j] == nums[j - 1]:
                continue
            while l < r:
                total = nums[j] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res