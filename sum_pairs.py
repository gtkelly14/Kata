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
    comp_index = None

    for outer_loop_index, outer_value in enumerate(list_of_integers):
        for inner_loop_index, inner_value in enumerate(list_of_integers[outer_loop_index+1:]):
            print(f"Outer: {outer_loop_index} Inner: {inner_loop_index}  comp_index: {comp_index}")
            if outer_value + inner_value == sum_value:
                if comp_index is None:
                    comp_index = inner_loop_index
                    first_value = outer_value
                    second_value = inner_value
                elif inner_loop_index < comp_index:
                    comp_index = inner_loop_index
                    first_value = outer_value
                    second_value = inner_value
                elif outer_loop_index == comp_index:
                    break

    if comp_index is None:
        return None

    return [first_value, second_value]



def sum_pairs_sol(lst, s):
    '''
    This was the codewars solution. It uses a set to store the values that have been seen.
    Pretty smart way of addressing this. I didn't think of using a set....

    
    Arguments:
        lst -- _description_
        s -- _description_

    Returns:
        _description_
    '''    
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)

if __name__ == "__main__":
    print(sum_pairs([1, 4, 8, 7, 3, 15], 8))
    print(sum_pairs([1, -2, 3, 0, -6, 1], -6))
    print(sum_pairs([20, -13, 40], -7))
    print(sum_pairs([1, 2, 3, 4, 1, 0], 2))
    print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
    print(sum_pairs([4, -2, 3, 3, 4], 8))
    print(sum_pairs([0, 2, 0], 0))
    print(sum_pairs([5, 9, 13, -3], 10))
