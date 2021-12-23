class Solution:

    ## method 1
    # def twoSum(self, numbers, target):
    #     # two point
    #     nums_index = [(v, index) for index, v in enumerate(numbers)]
    #     nums_index.sort()
    #     begin, end = 0, len(numbers) - 1
    #     while begin < end:
    #         curr = nums_index[begin][0] + nums_index[end][0]
    #         if curr == target:
    #             return [nums_index[begin][1] + 1, nums_index[end][1] + 1]
    #         elif curr < target:
    #             begin += 1
    #         else:
    #             end -= 1       
        
    ## method 2
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Two Points
        begin, end = 0, len(numbers) - 1
        while begin < end:
            curr = numbers[begin] + numbers[end]
            if curr == target:
                return [begin + 1, end + 1]
            elif curr < target:
                begin += 1
            else:
                end -= 1
