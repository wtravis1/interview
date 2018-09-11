##### Finding Geometric Sequences

import math
# Given a list (l) and a ratio (r), find the number of groups of 3 indices in the list such that:
# 1. a < b < c
# 2. {a, b, c} is a geometric sequence with a common ratio r

# Example:
# l = [1,1,5,25,25,125,625]
# r = 5

# quads = [
#     (0, 2, 3)
#     (0, 2, 4),
#     (1, 2, 3),
#     (1, 2, 4),
#     (2, 3, 5),
#     (2, 4, 5),
#     (3, 5, 6),
#     (4, 5, 6)
# ]
# count = 8

# Attempt 1, works correctly however extreamly slow for very large lists
def find_geo_seq(l, r):
    count = 0
    for a in range(len(l)-2):
        for b in range(a+1, len(l)-1):
            for c in range(b+1, len(l)):
                if (l[a] < l[b] and l[b] < l[c]):
                    if (l[b] == l[a] * r and l[c] == l[b] * r):
                        count += 1
    return count


# Attempt 2
# start by grouping all duplicate numbers together keeping
# track of how many of each number there were.
# this can be done because every time that number appears in a group there
# will be count(that number) other groups just like it
# if 2 or more numbers within a group have duplicates the same applies however,
# thier counts must be multiplied together
#
# r = 1 is a special case. In the instance that r = 1 combination can be
# used for each individual number and then added together at the end
def find_geo_seq_2(l, r):
    count = 0
    noDup = list(set(l))
    noDup.sort()
    myDict = {x: l.count(x) for x in noDup}

    if (r == 1):
        for num in noDup:
            count += get_combination(myDict[num])
    else:
        for a in range(len(noDup)-2):
            for b in range(a+1, len(noDup)-1):
                for c in range(b+1, len(noDup)):
                    if (noDup[b] == noDup[a] * r and noDup[c] == noDup[b] * r):
                        # print(noDup[a], noDup[b], noDup[c])
                        count += myDict[noDup[a]] * myDict[noDup[b]] * myDict[noDup[c]]
    return count

# Calculates n choose 3
# n is the number of each duplicate
def get_combination(n):
    return math.factorial(n) // math.factorial(n-3) // math.factorial(3)



test_cases = [
    ([1, 2, 2, 4], 2, 2),
    ([1,1,5,25,25,125,625], 5, 8),
    ([1, 3, 9, 9, 9, 9, 9, 10, 27, 81], 3, 17),
    ([345]*10000, 1, 166616670000),
    ([2, 2, 2, 4, 4, 4, 6, 6, 6], 1, 3),
    ([2, 2, 4, 4, 8, 8], 2, 8)
]

for case in test_cases:
    l, r, output = case
    print(find_geo_seq_2(l, r) == output)
