def checkSubarraySum(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        if sum(nums) < k and sum(nums) != 0:
            return False
        
        n = len(nums)
        
        for size in range(2, n + 1):
            
            for idx in range(n - size + 1):
                                
                if sum([nums[j] for j in range(idx, idx + size)]) % k == 0:
                    
                    return True

        return False


print(checkSubarraySum([0, 0], 1))