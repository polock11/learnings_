class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                
        return False
    
nums = [1,2,3]
solution = Solution()
val = solution.containsDuplicate(nums)
print(val)