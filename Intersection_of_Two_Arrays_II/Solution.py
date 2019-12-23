from typing import List

class Solution:
	"""
	Given two arrays, write a function to compute their intersection.
	"""

	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		dict = {}
		intersection = list()
		for ele in nums1:
			if ele not in dict.keys():
				dict[ele] = 1
			else:
				dict[ele] += 1
		for ele in nums2:
			if ele in dict.keys():
				if dict[ele] > 0:
					intersection.append(ele)
					dict[ele] -= 1
		return intersection

if __name__ == "__main__":
	solution = Solution()
	assert solution.intersect([1,2,2,1], [2,2]) == [2, 2], "Test case failed"
	print("All test cases passed succesfully")
