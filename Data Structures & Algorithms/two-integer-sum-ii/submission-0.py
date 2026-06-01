class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers are in order
        n = len(numbers)
        l = 0
        r = n - 1
        while l < r:
            curr = numbers[l] + numbers[r]
            print(curr)
            if curr == target:
                return [l+1, r+1]
            elif curr > target:
                r -= 1
            else:
                l += 1
        return []