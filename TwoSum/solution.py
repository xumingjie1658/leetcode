class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # The dict struct for index mapping.
        indexMapping = {}
        # the return array of the two elements' indexes
        numsIndexes = []

        # Build mapping relation.
        for index in range(len(nums)):
            indexMapping[nums[index]] = index

        for index in range(len(nums)):
            findingNum = target - nums[index]
            # We may not use the same element twice.
            if findingNum in indexMapping and indexMapping[findingNum] is not index:
                numsIndexes.append(index)
                numsIndexes.append(indexMapping[findingNum])
                break
        
        return numsIndexes

