class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #make maxHeap(*-1) or for -i in i
        #while len >1
        # smash largest stones(heappop then sumup)
        # add new stone to heap
        # repeat
        # return maxHeap[0]
        maxHeap=[]
        heapq.heapify(maxHeap)
        for i in stones:
            heapq.heappush(maxHeap, -i)

        while len(maxHeap)>1:
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)
            if stone1 != stone2:
                newStone = stone1 - stone2
                heapq.heappush(maxHeap, newStone)

        if maxHeap: 
            return -maxHeap[0] 
        else: 
            return 0



