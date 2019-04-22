# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        reverse_number = 0
        digit = x
        if x < 0:
            digit *= -1
        while digit > 0:
            reverse_number *= 10
            reverse_number += digit % 10
            digit //= 10
        if reverse_number > 2147483647:
            return 0

        elif x < 0:
            return int("-" + str(reverse_number))
        return reverse_number
