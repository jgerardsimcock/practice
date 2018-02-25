'''
The purpose of this exercise is to 
practice with the runtime improvements 
that sorting and using a greedy approach 
can afford you. 

The brute force approach to this algorithm 
runs in quadratic time and compares every value in the list
to every other value in the list. 

By sorting then doing some book keeping we can 
constrain our runtime to the cost of sort 
and the iteration through each of the values in the list. 

'''

def merge_tuple_times(time_list):

    #we need to sort so we at least
    #know that our start times are ordered
    #this enables us to make basic assumptions about
    #one piece of information
    sorted_list = sorted(time_list)

    merged_meetings = [sorted_list[0]]

    for current_meeting_start, current_meeting_end in sorted_list[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]



        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))


        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings