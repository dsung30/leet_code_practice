from typing import List

class Solution:
	"""
	Given a non-empty array of integers, every element appears twice except for one. Find that single one.
	"""

	def singleNumber(self, nums: List[int]) -> int:
		dict = {}
		for ele in nums:
			if ele not in dict.keys():
				dict[ele] = 0
			else:
				dict.pop(ele)
		return dict.popitem()[0]

if __name__ == "__main__":
	solution = Solution()

	assert solution.singleNumber([2,2,1]) == 1, "Test case 1 failed"
	assert solution.singleNumber([4,1,2,1,2]) == 4, "Test case 2 failed"

	print("All test cases passed succesfully")
