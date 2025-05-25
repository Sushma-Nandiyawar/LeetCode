class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # k = len(nums) - k
        # def quickSelect(l, r):
        #     pivot = nums[r]
        #     p = l
        #     for i in range(l, r):
        #         if nums[i]<= pivot:
        #             nums[p], nums[i] = nums[i], nums[p]
        #             p += 1
        #     nums[p], nums[r]= nums[r], nums[p]
        #     if k < p: return quickSelect(l,p-1)
        #     elif k > p : return quickSelect(p+1, r)
        #     else: return nums[p]
            
        # return quickSelect(0, len(nums) - 1)


        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]



