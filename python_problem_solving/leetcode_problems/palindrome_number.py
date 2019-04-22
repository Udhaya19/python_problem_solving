# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x > 0:
            original_list = list(map(int, str(x)))
            reverse_list = original_list[::-1]
            if original_list == reverse_list:
                return True
            else:
                return False
        if x < 0:
            return False
        if x==0:
            return True
