class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        C = A * (len(B) // len(A) + 2)#为了得到唯一可能含有B的组合字符串
        #验证是否含有
        if B in C:
            return (C.index(B) + len(B) + len(A) - 1) // len(A)#为了向上取整
        else:
            return -1


if __name__ == '__main__':
    print('abc'.index('bc'))
    s = Solution()
    print(s.repeatedStringMatch("abababaaba", "aabaaba"))