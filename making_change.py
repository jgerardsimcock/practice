'''
This problem asks us to find the number of ways we can
make change with a given set of coins for a given amount of money. 

Strategy
--------

1. For each denomination in the list of denominations
compute how many coins you need to reach or exceed the value amount. 

2. For each of those denominations, we then have the subproblem of 
computing how to reach or overshoot the remaining value amount.

'''

def making_change_bottom_up(amount, denominations):
    #create a data structure to store our answer
    ways_of_doing_n_cents = [0] * (amount * 1)

    #base case
    #there is only 1 way of getting zero coins
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        #I don't understand this
        for higher_amount in xrange(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin

            ways_of_doing_n_cents[higher_amount] += (
                ways_of_doing_n_cents[higher_amount_remainder]
                )

    return ways_of_doing_n_cents[amount]


def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]


   
