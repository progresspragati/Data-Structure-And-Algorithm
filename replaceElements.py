from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            a = sorted(arr[i+1:], reverse = True)
            arr[i] = a[0]
        arr[len(arr)-1] = -1
        return arr
    
    def replaceElements1(self, arr: List[int]) -> List[int]:
        right_max = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = right_max
            right_max = max(temp, right_max)
        return arr

result = Solution()
print(result.replaceElements1([2,4,5,3,1,2]))