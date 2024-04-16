import heapq
#min heap
Nums=[50,10,5,20,70,45,67,89]
heapq.heapify(Nums)
heapq.heappush(Nums,23)
heapq.heappush(Nums,15)
heapq.heappush(Nums,43)
print(Nums)
heapq.heappop(Nums)
print(Nums)
heapq.heapreplace(Nums,9)
heapq.heapreplace(Nums,19)
print(Nums)
Nums.remove(70)
print(Nums)
Nums.remove(4)
print(Nums)

