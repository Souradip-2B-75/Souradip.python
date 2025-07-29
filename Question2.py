class Solution:
    def elementFrequencies(self, arr):
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        result = []
        for key in freq:
            result.append([key, freq[key]])
        
        return result
sol = Solution()

arr1 = [10, 20, 10, 5, 20]
print(sol.elementFrequencies(arr1))  
arr2 = [10, 20, 20]
print(sol.elementFrequencies(arr2))