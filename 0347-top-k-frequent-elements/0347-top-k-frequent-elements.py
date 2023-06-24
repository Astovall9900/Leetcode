class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        items = list(freq.items())
        return [x[0] for x in sorted(items,reverse=True, key = lambda x:x[1])][:k]