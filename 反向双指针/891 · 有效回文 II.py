# https://www.lintcode.com/problem/891/

class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def valid_palindrome(self, s):
        # Write your code here
        left, right = self.find_diff(s, 0, len(s) - 1)
        
        if left >= right:
            return True

        return self.is_palindrome(s, left + 1, right)\
                or self.is_palindrome(s, left, right - 1)

    def find_diff(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            
            left += 1
            right -= 1

        return left, right
    
    def is_palindrome(self, s, left, right):
        left, right = self.find_diff(s, left, right)

        return left >= right
