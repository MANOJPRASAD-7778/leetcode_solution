class Solution:
    def trimMean(self, arr: list[int]) -> float:
        arr.sort()
        n = len(arr)
        k = n // 20
        
        return sum(arr[k:n-k]) / (n - 2*k)