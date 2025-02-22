# ECOR 1041 - Bonus

__author__ = "Mikhai Wilson"

__student_number__ = "101353707"

# ======================================================

# Exercise 1

def replicate(s: str) -> str:
    """
    Given a string, return a new strin that contains one or more copies of the argument.
    The number of copies is equals to the number of characters in the argument.

    Examples:
    >>> replicate('a')
    'a'
    >>> replicate('abc')
    'abcabcabc'
    >>> replicate('hello')
    'hellohellohellohellohello'
    """
    result = ""
    for i in range(len(s)):
        result += s
    return result

# ======================================================

# Exercise 2

def repeat_separator(word: str, sep: str, n: int) -> str:
    """
    Given a word, a separator, and a number n, return a long string with an of n occurrences
    of word, separated by the separator string sep.

    Examples:
    >>> repeat_separator("Word", "X", 3)
    'WordXWordXWord'
    >>> repeat_separator("This", "And", 2)
    'ThisAndThis'
    >>> repeat_separator("This", "And", 1)
    'This'
    """
    result = ""
    for i in range(n):
        result += word
        if i < n - 1:
            result += sep
    return result
    
# ======================================================

# Exercise 3

def has_pair(s: str, ch: str) -> bool:
    """
    Given a string s and a character ch, return True if s contains two occurrences of ch next
    to each other or then otherwise return False.

    Examples:
    >>> has_pair('abccd', 'c')
    True
    >>> has_pair('abcdc', 'c')
    False
    >>> has_pair('aabbc', 'a')
    True
    """
    for i in range(len(s) - 1):
        if s[i] == ch and s[i+1] == ch:
            return True
    return False

# ======================================================

# Exercise 4

def middle_way(list1: list[int], list2: list[int]) -> list[int]:
    """
    Given two lists that each contain three integer, return a new list containing the middle
    elements from both lists.

    example:
    >>> middle_way([1, 2, 3], [4, 5, 6])
    [2, 5]
    >>> middle_way([7, 7, 7], [8, 6, 7])
    [7, 6]
    >>> middle_way([5, 2, 9], [1, 4, 5])
    [2, 4]
    """
    return [list1[1], list2[1]]

# ======================================================

# Exercise 5

def make_ends(nums: list[int]) -> list[int]:
    """
    Given a list of integers, return a new list containing the first and last elements from the
    original list.

    example, 
    >>> make_ends([1, 2, 3, 4])
    [1, 4]
    >>> make_ends([1, 2, 3])
    [1, 3]
    >>> make_ends([1, 2])
    [1, 2]
    """
    return [nums[0], nums[-1]]
    
# ======================================================

# Exercise 6

def common_end(list1: list[int], list2: list[int]) -> bool:
    """
    Given two lists of integers that are not empty, return True if they have the same first
    element or the same last element. Otherwise, return False.

    >>> common_end([1, 2, 3], [7, 3])
    True
    >>> common_end([1, 2, 3], [7, 3, 2])
    False
    >>> common_end([1, 2, 3], [1, 3])
    True
    """
    return list1[0] == list2[0] or list1[-1] == list2[-1]

# ======================================================

# Exercise 7

def count_evens(nums: list[int]) -> int:
    """
    Given a list of integers, return the number of even integers in the list.
    >>> count_evens([2, 1, 2, 3, 4])
    3
    >>> count_evens([2, 2, 0])
    3
    >>> count_evens([1, 3, 5])
    0
    """
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

# ======================================================

# Exercise 8

def big_diff(nums: list[int]) -> int:
    """
    Given a list of integers, return the difference between the largest and smallest ones
    in the list.
    >>> big_diff([10, 3, 5, 6])
    7
    >>> big_diff([7, 2, 10, 9])
    8
    >>> big_diff([2, 10, 7, 2])
    8
    """
    smallest = nums[0]
    largest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return largest - smallest

# ======================================================

# Exercise 9

def has22(nums: list[int]) -> bool:
    """
    Given a list of integers, return True if the list contains a 2 next to a 2. Or then,
    return False.
    >>> has22([1, 2, 2])
    True
    >>> has22([1, 2, 1, 2])
    False
    >>> has22([2, 2, 1, 2])
    True
    """
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False

# ======================================================

# Exercise 10

def centered_average(nums: list[int]) -> float:
    """
    Given a list of numbers, return the arithmetic mean of all the numbers in the list, except
    for the smallest and largest values.
    >>> centered_average([1, 2, 3, 4, 100])
    3.0
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([-10, -4, -2, -4, -2, 0])
    -3.0
    """
    smallest = nums[0]
    largest = nums[0]
    total = 0
    for num in nums:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
        total += num
    return (total - smallest - largest) / (len(nums) - 2)

# ======================================================

# Exercise 11

def bank_statement(transactions: list[float]) -> list[float]:
    """
    Given a list of floating point numbers, return a new list containing three numbers: the first
    will be the sum of the deposits, the second (a negative number) will be the sum of the
    withdrawals, and the third will be the current account balance.
    >>> bank_statement([100.0, -25.0, 50.0, -10.0])
    [150.0, -35.0, 115.0]
    >>> bank_statement([20.0, -5.0, -10.0, 30.0])
    [50.0, -15.0, 35.0]
    >>> bank_statement([50.0, -50.0, 100.0])
    [150.0, -50.0, 100.0]
    #Note that this function rounds the answer to two decimal places, i hope thats ok!
    """
    deposits = 0
    withdrawals = 0
    for transaction in transactions:
        if transaction > 0:
            deposits += transaction
        else:
            withdrawals += transaction
    balance = deposits + withdrawals
    return [round(deposits, 2), round(withdrawals, 2), round(balance, 2)]

# ======================================================

# Exercise 12

def reverse(nums: list[int]) -> list[int]:
    """
    Given a list, return a new list that contains all the list parts from the original list in
    reverse order.
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse([3, 2, 1])
    [1, 2, 3]
    >>> reverse([])
    []
    #This function is super cool, reversing the list is fun :D
    """
    new_list = []
    for i in range(len(nums) - 1, -1, -1):
        new_list.append(nums[i])
    return new_list
