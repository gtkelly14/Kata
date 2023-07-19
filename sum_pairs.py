'''
Find numbers that sum to a given number
'''


def sum_pairs(list_of_integers, sum_value):
    '''
    Function to iterate through a list and find a pair of vaules that sum to a given value

    Arguments:
        ints -- List of integers to check
        sum_value -- Value to match

    Returns:
        tuple of numbers that sum to the given value. 
    '''
    first_value = 0
    second_value = 0
    second_index = None


    for outer_loop_index in range(len(list_of_integers)):
        for inner_loop_index in range(outer_loop_index+1, len(list_of_integers)):
            if list_of_integers[outer_loop_index] + list_of_integers[inner_loop_index] == sum_value:
                if second_index is None:
                    first_value = list_of_integers[outer_loop_index]
                    second_value = list_of_integers[inner_loop_index]
                    second_index = inner_loop_index
                elif inner_loop_index < second_index:
                    first_value = list_of_integers[outer_loop_index]
                    second_value = list_of_integers[inner_loop_index]
                    second_index = inner_loop_index


                return [list_of_integers[outer_loop_index], list_of_integers[inner_loop_index]]

    return None


if __name__ == "__main__":
    print(sum_pairs([1, 4, 8, 7, 3, 15], 8))
    print(sum_pairs([1, -2, 3, 0, -6, 1], -6))
    print(sum_pairs([20, -13, 40], -7))
    print(sum_pairs([1, 2, 3, 4, 1, 0], 2))
    print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
    print(sum_pairs([4, -2, 3, 3, 4], 8))
    print(sum_pairs([0, 2, 0], 0))
    print(sum_pairs([5, 9, 13, -3], 10))
