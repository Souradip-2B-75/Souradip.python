class Solution:
    def rotateByOne(self, arr):
        if not arr:
            return arr
        last = arr[-1]   
        arr.pop()       
        arr.insert(0, last)    
        return arr
sol = Solution()

arr1 = [1, 2, 3, 4, 5]
print(sol.rotateByOne(arr1))

arr2 = [9, 8, 7, 6, 4, 2, 1, 3]
print(sol.rotateByOne(arr2))