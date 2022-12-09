# Implement function count_numbers that accepts a sorted list of unique integers and, efficiently with respect to time used, counts the number of list elements that are less than the parameter less_than.
#
# For example, count_numbers([1, 3, 5, 7], 4) should return 2 because there are two list elements less than 4.

def count_numbers(sorted_list, less_than):

    mid = len(sorted_list)//2 - 1

    # end conditions
    if len(sorted_list) == 0:
        return 0
    elif sorted_list[-1] < less_than:
        return len(sorted_list)
    elif sorted_list[mid] < less_than <= sorted_list[mid+1]:
        return mid + 1
    elif sorted_list[mid] == less_than:
        return mid

    # recursion to parse through bst
    if sorted_list[mid] > less_than:
        return count_numbers(sorted_list[:mid+1], less_than)
    elif sorted_list[mid] < less_than:
        return (mid + 1) + count_numbers(sorted_list[mid+1:], less_than)



if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11]
    print(count_numbers(sorted_list, 12))