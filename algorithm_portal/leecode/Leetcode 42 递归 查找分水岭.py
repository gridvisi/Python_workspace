'''

黑色的是柱子，蓝色的是水。
求最多能盛多少水。

解法
有很多解法，比如扫描数组，算出每个位置上到左边、右边的最高柱子的高度， O（n）时间复杂度

下面的解法是找分水岭，比如从左往右遍历，只要找到第一个高度大于最左侧的柱子的，它就是分水岭，
这时候就能确定前面的水位。然后后面的和前面的就没关系了，递归执行这个算法。

到最后一段，可能没有更高的柱子了，找不到分水岭，但是可以直接把数组前后颠倒（reverse），
再递归调用一次就可以了。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水
（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# https://leetcode-cn.com/problems/trapping-rain-water/
height = [0,1,0,2,1,0,1,3,2,1,2,1]
class Solution:
    def trap(self, height):   # -> : list[int] int:
        cnt = len(height)
        if cnt < 3: return 0
        if cnt == 3:
            if height[0] > height[1] < height[2]:
                return min(height[0],height[2]) - height[1]
            return 0
        for l in range(cnt):
            if height[l] > 0: break
        hl = height[l]
        cur = l + 1
        f = False
        v = 0
        while cur < cnt:
            if height[cur] < hl:
                f = True
            else:
                if f:
                    for i in range(cur-1, l, -1):
                        if height[i] < hl:
                            v += hl - height[i]
                return self.trap(height[cur:]) + v
            cur += 1
        height.reverse()
        return self.trap(height)

myRiver = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(myRiver.trap(height))