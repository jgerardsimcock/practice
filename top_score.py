def sort_score(value_list, top_score):

    # create our data structure that represents 
    # where we have values
    score_counts = [0] * (top_score + 1)

    #put a 1 in the indexes where we have a value
    #most of the indexes will be zero
    for item in value_list:
        score_counts[item] +=1 


    sorted_list = []


    #now since we want to return a sorted list from highest to lowest
    #we need to iterate backwards.
    for score in xrange(len(top_score), -1, -1, -1):
        #score is the index and count is either one or zero
        count = num_counts[score]

        #so we append our value, score either zero or 1 times. 
        for time in xrange(count):

            sorted_list.append(score)

    return sorted_list

