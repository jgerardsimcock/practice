'''
Find the max value in an array and subtract the lowest value
Constraints include max value must come after the min value in the array.
If array max is before then the highest value that is after the min value 
should be used. 

Key to this algorithm is the definition of maximum profit

which is a function of some value minus the minimum value so far. 
As we iterate through the list we need to define:

maximum_value_so_far = None

minimum_value_so_far = None


Since there is only one iteration of the array, this algo runs in linear time

'''
import numpy as np
f = np.random.randint(0,100,10)


def get_max_profit(stock_prices_array):

    if len(stock_prices_array) < 2:
        raise ValueError('stock_prices_array must be gt 2 values')

    #we initialize a value as min
    #this is true until it is not
    #we make an assumption about the state 
    #of the world until we update our model
    min_price = stock_prices_array[0]
    #we initialize a value of max based on
    #the minimum possible amount of data we have to 
    #make a decision
    maxprofit = stock_prices_array[1] - minprice

    #we need to start at 1 because its possible our index 1 value is lower than
    #index 0 value and we want to reassign our min_price value
    for i in xrange(1, len(stock_prices_array)):
        current_price = stock_prices_array[i]

        #set up a calculation to evaluate our potential state shift
        potential_profit = current_price  min_price

        #evaluate to see if our potential profit has exceeded our maxprofit
        #is the number we are looking at the highest wrt our low
        maxprofit = max(potential_profit, maxprofit)

        #evaluate to see if we need to update our min 
        #is what we are looking at less than our min
        min_price = min(current_price, min_price)

    return maxprofit