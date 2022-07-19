"""
121. Best Time to Buy and Sell Stock
Easy

16849

558

Add to List

Share
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
Accepted
2,261,043
Submissions
4,171,170
Seen this question in a real interview before?

Yes

No
"""
from bisect import insort_right
from typing import List

def gen_diff_window(length:int):
    try:
        string = ''
        for i in range(length-1):
            # print(0, length - 1 - i)
            num_list =  []
            for j in range(i+1):
                num_list.append(((j, length-1-i+j)))
            yield num_list
                # print(i, length-1-i+j)
    except Exception as e:
        print("error in gen_diff_window genrator fn", str(e))

def last_list_match(num_list, N):
    match_pos = 0
    for i in range(len(num_list)):
        if num_list[i] == N:
            match_pos = i
    return match_pos

def maxProfit(prices: List[int]) -> int:
    # prices  = [7,1,5,3,6,4]
    # prices  = [7,6,4,3,1]
    prices  = [4,11,1,2,7]
    # prices  = [2,7,1,4]
    gen = gen_diff_window(len(prices))
    arr_sorted  = prices[:]
    arr_sorted.sort()
    flag = True 
    while(True and flag == True):
        try:
            max = 0
            t = next(gen)
            max = 0
            profit = 0
            profit_list = []
            for i in t: 
                first =  prices.index(arr_sorted[i[0]])
                last = last_list_match(prices, arr_sorted[i[1]])
                if (first < last):
                    profit = prices[last] - prices[first]
                    insort_right(profit_list, profit)
                
            if profit_list:
                profit = profit_list[-1]
                flag = False
                    
        except StopIteration:
            break
    return profit

def soln_2(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            
    return max_profit

if __name__=="__main__":
    prices = [4,11,1,2,7]    
    
    max_profit = soln_2(prices=prices)

    print(max_profit)
    