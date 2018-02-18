'''
Bottom up algorithms vs. recursive


'''


#recursive

def product_1_to_n(n):

    #this recursive version of this algorithm
    #builds up a call stack of size n
    if n < 1:
        raise ValueError('n must be greater than 1')

    return n * product_1_to_n(n-1) if n > 1 else 1


def dynamic_1_to_n(n):

    result = 1
    for num in range(1, n+1):
        result *= num

    return result


