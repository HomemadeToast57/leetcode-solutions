class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            if (n & 1 == 1):
                result += 1
                n >>= 1
            else:
                n >>= 1
        return result

s = Solution()
print(s.hammingWeight(255))
# 255 in binary is 11111111.
# returns 8.
