'''
Given a list of integers, find the highest product you 
can get from three of the integers. 

'''

def highest_product(int_list):


    int_list = sorted(int_list, reverse=True)
    
    highest_product_of_three = reduce(lambda x,y:  x* y in int_list[:2])

    
    highest_product_of_two = int_list[0] * int_list[1]
    
    highest = max(int_list[0], int_list[1])
    
    lowest_product_of_two = int_list[0] * int_list[1]
    
    lowest = min(int_list[0], int_list[1])

    for v in int_list[2:]:
        current = v


        highest_product_of_three = max(highest_product_of_three,
                                        current * highest_product_of_two,
                                        current * lowest_product_of_two)


        highest_product_of_two = max(highest_product_of_two, 
                                     current * highest, 
                                     current * lowest)

        lowest_product_of_two = min(lowest_product_of_two,
                                    current * lowest,
                                    current * highest)

        highest = max(current, highest)

        lowest = min(current, lowest)


    return highest_product_of_three

