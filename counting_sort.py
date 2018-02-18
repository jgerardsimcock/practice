

def counting_sort(the_list, max_value):

# list of 0's at indices 0...max_value
num_counts = [0] * (max_value+1)

# populate num_counts
# replace 0 with 1
# this puts a 1 at the index of the value in the list
# for example, in the_list if we have 10 in the list,
# we'll change 0 to 1 and index 10
for item in the_list:
    num_counts[item] += 1

# populate the final sorted list
# this is where we store our final result
sorted_list = []

# for each item in num_counts

for item, count in enumerate(num_counts):

    # most of our values will be zero here.
    # when we do have a value its index will
    # represent its value 
    # for the number of times the item occurs
    for time in range(count):

        # add it to the sorted list
        sorted_list.append(item)

return sorted_list