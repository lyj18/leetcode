class Solution:

    def longestCommonPrefix(self, strs):
        result = ""
        if len(strs) == 0:
            return ''
        for j in range(len(strs[0])):#注意i，j循环的先后顺序
            for i in range(len(strs)):
                if j >= len(strs[i]):#防止index过大
                    return result
                elif strs[0][j] != strs[i][j]:
                    return result
            result+= strs[0][j]
        return result#单个字符 最后return
