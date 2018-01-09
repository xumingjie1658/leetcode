from solution import Solution

solution = Solution()

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    numsIndex = solution.twoSum(nums, target)
    print(numsIndex)