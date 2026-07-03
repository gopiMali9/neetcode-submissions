class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dct = {}

        for i in set(nums):
            dct[i] = nums.count(i)

        _items = [(i,j) for i,j in dct.items()]

        sorted_values = sorted(_items,key= lambda x : x[1],reverse=True)

        output = [i for i,j in sorted_values ]

        return output[:k]