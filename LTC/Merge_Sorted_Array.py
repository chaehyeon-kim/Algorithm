class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l1 = m - 1
        l2 = n - 1
        l = m + n - 1
        while l1 >= 0 and l2 >= 0:
            if nums1[l1] < nums2[l2]:
                nums1[l] = nums2[l2]
                l2 -= 1
            else:
                nums1[l] = nums1[l1]
                l1 -= 1
            l -= 1
        if l2 >= 0:
            nums1[:l+1] = nums2[:l2+1]
        return nums1
