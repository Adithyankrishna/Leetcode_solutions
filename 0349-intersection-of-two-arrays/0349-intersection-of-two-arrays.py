class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        seen1 = set(nums1)
        seen2 = set(nums2)

        for num in seen1:
            if num in seen2:
                res.append(num)
        return res