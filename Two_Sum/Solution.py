from typing import List

class Solution:
	"""
	Problem:

	Say you have an array for which the ith element is the price of a given stock on day i.

	Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

	Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
	"""

	def twoSum(self, nums: List[int], target: int) -> List[int]:
		sumDict = {}
		for i in range(len(nums)):
			diff = target - nums[i]
			if diff in sumDict.keys():
				return [sumDict[diff], i]
			else:
				sumDict[nums[i]] = i
		return None

if __name__ == "__main__":
	solution = Solution()
	assert solution.twoSum(nums = [2, 7, 11, 15], target = 9) == [0, 1], "Test case failed"

	print("All test cases passed succesfully")
