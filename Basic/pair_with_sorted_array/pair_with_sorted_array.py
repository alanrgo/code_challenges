# https://practice.geeksforgeeks.org/problems/pair-with-given-sum-in-a-sorted-array/0
# You are given an array A of size N. You need to find all pairs in the array that sum to a number K. 
# If no such pair exists then output will be -1. The elements of the array are distinct and are in sorted order.
# Note: (a,b) and (b,a) are considered same. Also, an element cannot pair with itself, i.e., (a,a) is invalid.
#
# Input:
# The first line of input is T denoting the number of testcase. T testcases follow. Each testcase contains three lines of input. 
# The first line is the size of array N. The second line contains N elements separated by spaces. The third line contains the sum K.
#
# Output:
# For each testcase, print all the pairs such that there sum is equal to K.

def binary_search(array, current_left, value):
    r = len(array) -1
    l = current_left

    while l<= r:
        m = int((l + r)/2)
        if array[m] == value:
            return m
        if array[m] < value:
            l = m + 1
        else: 
            r = m - 1
    return -1

n_tests = input()

for i in range(0, int(n_tests)):
    size = input()
    numbers = [int(n) for n in input().split()]
    k = int(input())
    found = 0
    for y in range(0, int(len(numbers)/2)):
        current_value = numbers[y]
        looking_for = k - current_value
        new_index = binary_search(numbers, y + 1, looking_for)
        if new_index != -1:
            found = found + 1
            print('{0} {1} {2}'.format(numbers[y], numbers[new_index], k))
    if found == 0:
        print(-1)