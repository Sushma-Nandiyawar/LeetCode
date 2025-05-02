class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        element = majority = 0

        for n in nums:
            hash[n] = 1 + hash.get(n,0)
            if hash[n] >majority:
                element=n
                majority = hash[n]

        return element