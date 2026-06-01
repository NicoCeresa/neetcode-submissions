class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return: k most freq elements in arr
        # counter -> sort counter -> loop k times
        counter = dict()
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        out = []
        for i in range(k):
            max_count = max(counter, key=counter.get)
            out.append(max_count)
            counter[max_count] = -1
        return out