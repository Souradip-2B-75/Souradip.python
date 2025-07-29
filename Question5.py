class Solution:
    def isSortedAndRotated(self, arr):
        count = 0
        n = len(arr)
        
        for i in range(n):
            if arr[i] > arr[(i + 1) % n]:
                count += 1
        
        return count <= 1
sol = Solution()

arr1 = [3, 4, 5, 1, 2]
print("YES" if sol.isSortedAndRotated(arr1) else "NO")
arr2 = [3, 4, 6, 1, 2, 5]
print("YES" if sol.isSortedAndRotated(arr2) else "NO")