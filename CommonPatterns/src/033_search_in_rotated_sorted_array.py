class Solution(object):
        
    def search(self, nums, target):
        def helper(nums, target, head):
            if len(nums) == 0:
                return -1
            if len(nums) == 1 and nums[0] == target:
                return head
            
            if len(nums) == 2:
                if nums[0] == target:
                    return head
                if nums[1] == target:
                    return head+1
                return -1


            mid = len(nums)/2
            end = len(nums)-1

            b = nums[0]
            m = nums[mid]
            e = nums[end]

            if b == target:
                return head
            if m == target:
                return head+mid
            if e == target:
                return head+end

            if b < e:
                if b < target and target < m:
                    return helper(nums[0:mid], target, head)
                if m < target and target < e:
                    return helper(nums[mid:end], target, head+mid)
                return -1
            else:
                val = helper(nums[0:mid], target, head)
                if val != -1:
                    return val
                return helper(nums[mid:-1], target, head+mid)

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return helper(nums, target, 0)