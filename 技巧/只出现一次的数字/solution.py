from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            ans ^= x
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2, 2, 1]))        # 1
    print(s.singleNumber([4, 1, 2, 1, 2]))  # 4
