class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) < 3:
            return []
        
        res = []
        nums.sort()
        
        if nums[0] > 0 or nums[-1] < 0:
            return res
        
        for i in range(0, len(nums)-2):    
            if nums[i] > 0:
                return res
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            j = i + 1
            k = len(nums) - 1

            while j < k:
                _3sum = nums[i] + nums[j] + nums[k] 
                if _3sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while k > j and nums[k] == nums[k-1]:
                        k -= 1
                        
                    j += 1
                    k -= 1
                elif _3sum > 0:
                    k -= 1
                else:
                    j += 1
                    
        return res    