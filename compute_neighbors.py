'''

The purpose of this algorithm is to compute the product
of all values in an array except the value currently indexed
by the iteration.

[1, 7, 3, 4] => [84, 12, 28, 21] => [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]


at each shift along the length of the array I want to know what the other
values in the array are

I want to loop through the array and collect the following information
in each index I need the values from the other indexes. 

how to keep 

'''

def compute_neighbors(index_array):


    products_except_at_index  = [None] * len(index_array)

    product_so_far = 1
    for i in xrange(index_array):

        #this is our value before the index
        products_except_at_index[i] = product_so_far
        product_so_far *= index_array[i]


    product_so_far = 1
    for i in xrange(len(index_array) - 1, -1, -1):
        products_except_at_index[i] *= product_so_far
        product_so_far *= index_array[i]


    return products_except_at_index















