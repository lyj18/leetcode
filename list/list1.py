class Solution:
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int 返回数值是整数，但输出的答案是数组
        输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的
        思考1：遍历之后查到重复之后，替换成后面的元素
        """
        flag = len(nums)-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    nums[j],nums[flag] = nums[flag],nums[j]
                    flag -= 1
                    if j == flag:
                        return (j+1)
                        break


nums = [1,1,2]
print(Solution.removeDuplicates(nums))
print(Solution.)
