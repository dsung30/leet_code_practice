from typing import List

class Solution:
	"""
	Problem:

	Say you have an array for which the ith element is the price of a given stock on day i.

	Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

	Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
	"""

	def maxProfit(self, prices: List[int]) -> int:
		
		# Initialize parameters
		hold = False
		buyPrice = -1
		profit = 0

		for i in range(len(prices)):

			if i < len(prices) - 1:
				# Buy if holding nothing and next day price is higher than current
				if not hold and prices[i] < prices[i + 1]:
					buyPrice = prices[i]
					hold = True
				# Sell if holding something and next day price is lower than current
				elif hold and prices[i] > prices[i + 1]:
					profit += prices[i] - buyPrice
					hold = False
			else:
				if hold:
					profit +=  prices[i] - buyPrice

		return profit

if __name__ == "__main__":
	
	solution = Solution()

	assert solution.maxProfit([7,1,5,3,6,4]) == 7, "Test case 1 failed"
	assert solution.maxProfit([1,2,3,4,5]) == 4, "Test case 2 failed"
	assert solution.maxProfit([7,6,4,3,1]) == 0, "Test case 3 failed"

	print("All tests passed succesfully")


