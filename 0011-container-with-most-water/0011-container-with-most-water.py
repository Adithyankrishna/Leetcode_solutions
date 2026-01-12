class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height)-1
        low = 0
        area = 0

        while left != right:
            low = min(height[left], height[right])
            width = right - left
            area = low * width
            maxarea = max(maxarea,area)
            if height[right] >= height[left]:
                left +=1
            elif height[left] >= height[right]:
                right -= 1
        return maxarea
        