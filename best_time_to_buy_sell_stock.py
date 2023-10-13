def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    temp_max = 0
    i = 0
    j = 1
    while j < len(prices):
        if prices[j] > prices[i]:
            temp_max = max(prices[j] - prices[i], temp_max)
        else:
            i = j
        j += 1
    return temp_max