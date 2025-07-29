class Solution:
    def insertAtEnd(self, arr, ele):
        arr.append(ele)   
        return arr
sol = Solution()

arr1 = [10, 20, 30, 40]
print(sol.insertAtEnd(arr1, 50))  
arr2 = []
print(sol.insertAtEnd(arr2, 20))