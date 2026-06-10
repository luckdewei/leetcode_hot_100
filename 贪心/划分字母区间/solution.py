from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """记录每个字母最后出现位置，贪心扩展片段"""
        last = {ch: i for i, ch in enumerate(s)}
        ans = []
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                ans.append(end - start + 1)
                start = i + 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))
    # [9, 7, 8]
