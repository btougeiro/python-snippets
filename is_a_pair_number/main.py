"""
Write a function that receives an array of numbers, for example [9,3,9,3,7,7,9], and returns
the number that doesn't have a pair. In the example we have 9 repeated 3 times, a pair of 3s
and a pair of 7s, which means that we have a 9 without a pair.
"""

def is_a_pair(numbers):
    return {num for num in numbers if numbers.count(num) > 2}

print(is_a_pair([3,3,9,3,7,7,7,9]))

"""
output -> {3, 7}
"""

print(is_a_pair([9,3,9,3,7,7,9]))

"""
output -> {9}
"""
