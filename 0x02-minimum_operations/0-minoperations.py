#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor
execute only two operations in the file: Copy ALL  and Paste.
Given a number n write a method that calculates the fewest
of operations needed to result in exactly n H characters
in the file
"""


def minOperations(n):
    """
    function that calculates the fewest number of calculations
    """
    if n <= 1:
        return 0
    # this checks if n is less than or equal 1. if it is the
    # function returns 0 coz no operations are needed when n
    # n is 0(nothig to do) or 1 (already have one 'H')

    operations = 0
    # keeps track of the tt no. of operations performed

    factor = 2
    """
    finds factor of the numbers n. Starting with a factor
    of 1 would be ineffective coz copying and pasting a single
    character ('H') does not change the length of the string
    it merely replicates the existing single character
    Therefore,the smallest meaningful factor to start with is
    if n is divisible by 2, it means we can double the length of
    the str by copying the entire str (when its half n) and then
    pasting it once, this is more efficient than pasting one char at a time
    if n is not divisible by 2, the code will then check the next
    possible factor(3, 4, 5, and so on) until it finds a
    factor of n.Each time a factor is found it reps an efficient
    way to expand the str to reach the target n
    """

    while n > 1:
        while n % factor == 0:
            operations += factor
            # this line increments operations by the value of factor
            # each time this line is executed,it simulates the process
            # of Copy all followed by factor - 1 paste operations
            n //= factor
            # updates n by dividing it by factor, effectively reduces
            # in a way that reflects the pasting of a str of len factor
        factor += 1
        # increments factor by 1, used to check the next possible
        # factor of n

    return operations
