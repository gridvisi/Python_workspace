'''
示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
思路：

双指针法。
每次循环二者中高度小的那个指针往中心移动，因为这样可以抵消宽度减小带来的影响，更有可能得到面积更大的矩形。
'''


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo, hi = 0, len(height) - 1
        res = 0
        while (lo < hi):
            if height[lo] > height[hi]:
                area = height[hi] * (hi - lo)
                hi -= 1
            else:
                area = height[lo] * (hi - lo)
                lo += 1
            # print area
            res = max(area, res)
        return res
