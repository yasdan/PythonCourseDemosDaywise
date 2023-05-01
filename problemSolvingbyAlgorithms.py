# # Greedy algorithm based program demo
def interval_scheduling(stimes, ftimes):
    """Return largest set of mutually compatible activities.

    This will return a maximum-set subset of activities
    (numbered from 0 to n - 1) that are mutually compatible.
    Two activities are mutually compatible if the start time
     of one activity is not less then the finish time of the other.

    stimes[i] is the start time of activity i.
    ftimes[i] is the finish time of activity i.
    """
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(stimes)))
    # sort according to finish times
    index.sort(key=lambda i: ftimes[i])

    maximal_set = set()
    prev_finish_time = 0
    for i in index:
        if stimes[i] >= prev_finish_time:
            maximal_set.add(i)
            prev_finish_time = ftimes[i]

    return maximal_set


def intervelScheduleGreedyaproach():
    n = int(input('Enter number of activities: '))
    stimes = input('Enter the start time of the {} activities in order: '
                   .format(n)).split()
    stimes = [int(st) for st in stimes]
    ftimes = input('Enter the finish times of the {} activities in order: '
                   .format(n)).split()
    ftimes = [int(ft) for ft in ftimes]
    ans = interval_scheduling(stimes, ftimes)
    print('A maximum-size subset of activities that are'
          ' mutually compatible is', ans)
0
#intervelScheduleGreedyaproach()

# Find max crossing subarray with divide & conquer technique
def find_max_subarray(alist, start, end):
    """Returns (l, r, m) such that alist[l:r] is the maximum subarray in
    A[start:end] with sum m. Here A[start:end] means
    all A[x] for start <= x < end."""
    # base case
    if start == end - 1:
        return start, end, alist[start]
    else:
        mid = (start + end) // 2
        left_start, left_end, left_max = find_max_subarray(alist, start, mid)
        right_start, right_end, right_max = find_max_subarray(alist, mid, end)
        cross_start, cross_end, cross_max = find_max_crossing_subarray(alist, start, mid, end)
        if (left_max > right_max and left_max > cross_max):
            return left_start, left_end, left_max
        elif (right_max > left_max and right_max > cross_max):
            return right_start, right_end, right_max
        else:
            return cross_start, cross_end, cross_max

def find_max_crossing_subarray(alist, start, mid, end):
    """Returns (l, r, m) such that alist[l:r] is the maximum subarray within
    alist with start <= l < mid <= r < end with sum m. The arguments start, mid,
    end must satisfy start <= mid <= end."""
    sum_left = float('-inf')
    sum_temp = 0
    cross_start = mid
    for i in range(mid - 1, start - 1, -1):
        sum_temp = sum_temp + alist[i]
        if sum_temp > sum_left:
            sum_left = sum_temp
            cross_start = i

    sum_right = float('-inf')
    sum_temp = 0
    cross_end = mid + 1
    for i in range(mid, end):
        sum_temp = sum_temp + alist[i]
        if sum_temp > sum_right:
            sum_right = sum_temp
            cross_end = i + 1
    return cross_start, cross_end, sum_left + sum_right


def divideandConquer():
    global start, end
    alist = input('Enter the list of numbers: ')
    alist = alist.split()
    alist = [int(x) for x in alist]
    start, end, maximum = find_max_subarray(alist, 0, len(alist))
    print('The maximum subarray starts at index {}, ends at index {}'
          ' and has sum {}.'.format(start, end - 1, maximum))


#divideandConquer()

#Dynamic programing example
def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n == 0:
        return 0
    # r[i] will contain the ith Fibonacci number
    r = [-1] * (n + 1)
    r[0] = 0
    r[1] = 1
    for i in range(2, n + 1):
        r[i] = r[i - 1] + r[i - 2]

    return r[n]


def dynamicProFibonocci():
    n = int(input('Enter n: '))
    ans = fibonacci(n)
    print(f'The {n}th Fibonacci number: {ans}')
dynamicProFibonocci()
