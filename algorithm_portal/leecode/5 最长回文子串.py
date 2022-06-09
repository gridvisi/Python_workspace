#https://blog.csdn.net/qq_32424059/article/details/88855423

# https://leetcode-cn.com/problems/longest-palindromic-substring/

print(True ^ False)
print(True ^ True)
print(False ^ False)

s = "babad"


class Solution:
    def longestPalindrome(self, s: str):
        if s == s[::-1]: return s
        ans, l, maxx, target = [], len(s)+1, -314, 0
        for i in range(l):
            for j in range(i+1, l):
                if s[i:j] == s[i:j][::-1]:
                    ans.append(s[i:j])
        return max(ans, key=len, default='')
    def longestPalindrome2(self, s: str):
        l, r, ch = 0, len(s), 0
        while l<=r:
            if s[l:r] == s[l:r][::-1]:
                return s[l:r]
            if ch % 2 == 0:
                l += 1
            else:
                r -= 1
            ch += 1
print(Solution.longestPalindrome(0, s))


class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]
