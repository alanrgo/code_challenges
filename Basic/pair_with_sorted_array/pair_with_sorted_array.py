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
array = [0] * 10000000

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