'''
    You are given two integer arrays nums1 and nums2, sorted in 
    non-decreasing order, and two integers m and n, representing 
    the number of elements in nums1 and nums2 respectively.
    Merge nums1 and nums2 into a single array sorted in non-
    decreasing order.
    The final sorted array should not be returned by the function,
    but instead be stored inside the array nums1. To accommodate 
    this, nums1 has a length of m + n, where the first m elements
    denote the elements that should be merged, and the last n 
    elements are set to 0 and should be ignored. nums2 has a 
    length of n.
'''

### This question make funadamentals clear about array methods.
### insert(), remove(), pop()
class Solution:
    def merge(self, nums1, m: int, nums2, n: int):

        if nums1 == [] or nums2 == []:
            return
        else:
            i = 0
            count = m
            while len(nums2) > 0 and i < m+n:
                if nums1[i] > nums2[0]:
                    if i < count: 
                        nums1.insert(i,nums2[0])
                        nums1.pop(m+n)
                        nums2.remove(nums2[0])
                        count += 1
                if i >= count:  
                    nums1[i] = nums2[0]
                    nums2.remove(nums2[0])
                i += 1
                print(nums1)
            
a = Solution()
a.merge(nums1 = [-1,0,0,3,3,3,0,0,0], m = 6, nums2 = [1,2,2], n = 3)