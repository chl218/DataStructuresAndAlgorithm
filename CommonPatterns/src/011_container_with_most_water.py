class Solution:
    def maxArea(self, height: List[int]) -> int:   
        b = 0
        e = len(height) - 1
        
        area = 0
        while b < e:
            
            l = e - b
            h = min(height[b], height[e])
            area = max(area, l*h)
            
            if height[b] < height[e]:
                b += 1
            else:
                e -= 1
            
        return area