class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]
sol = Solution()

print(sol.isPalindrome("madam")) 
print(sol.isPalindrome("car")) 
