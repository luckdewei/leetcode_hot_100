from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """排序 + 双指针：O(n²) 时间，O(1) 额外空间（不含输出）"""
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return ans


# --- 本地测试 ---
if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    # [[-1, -1, 2], [-1, 0, 1]]
    print(s.threeSum([0, 1, 1]))  # []
    print(s.threeSum([0, 0, 0]))  # [[0, 0, 0]]
