"""


This is a demo task.

Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].

"""
# 100
def solution(A):
    # write your code in Python 3.6
    ddict = {}
    maxval = float("-inf")
    for key in A:
        if key > 0:
            if key > maxval:
                maxval = key
            if key not in ddict:
                ddict[key] = 1
    if not ddict:
        return 1
    for i in range(1, maxval + 1):
        if i not in ddict:
            return i
    return maxval + 1