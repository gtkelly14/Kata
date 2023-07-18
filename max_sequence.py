'''
Max Sequence Kata `
'''


def max_sequence(arr):
    '''
    Determine maximum contiguous sum from an array passed into the function

    Arguments:
        arr -- list of numbers

    Returns:
        an integer holding the maximum sum. O if empty array or all numbers are negative

    '''

    if len(arr) == 0:
        return 0

    # Check for positive numbers
    if not max(arr) > 0:
        return 0

    max_sum = 0
    cur_sum = 0
    for start in range(len(arr)):

        for j in range(start, len(arr)):
            cur_sum = sum(arr[start:j+1])
            if cur_sum > max_sum:
                max_sum = cur_sum

    return max_sum


if __name__ == "__main__":

    print("Hello World")
    print(f"{max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])} should equal 6")
    print(
        f"{max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4])} should equal 0")
    print(
        f"{max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10,-32, 44, -26, -34, 43, 43])} should equal 155")
