class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        dict = {}
        
        for i, num in enumerate(numbers):
            if target - num in dict:
                return [dict[target-num] + 1, i + 1]
            else:
                dict[num] = i
                
        return [-1, -1]