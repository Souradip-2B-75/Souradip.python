class Solution:
    def findfrequency(self, arr, x):
        count = 0
        for num in arr:
            if num == x:
                count += 1
        return count   
sol = Solution()
arr = [1, 9, 3, 8, 7, 2, 3]
x = 1
print("Frequency of", x, "is:", sol.findfrequency(arr, x))