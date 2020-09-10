'''
Implementation of Binary Min Heap using heapq module..
By default this module will give min Heap.
'''
import heapq as h
heap=[]
h.heapify(heap)
def printheap(heap):
    for i in heap:
        print(-1*i,end=' ')
    print(" ")

#insert
h.heappush(heap,-1*100)
h.heappush(heap,-1*98)
h.heappush(heap,-1*120)
h.heappush(heap,-1*70)
printheap(heap)
print(-1*h.heappop(heap)) #pop min element
print(-1*h.heappushpop(heap,-1*200))
printheap(heap)
print(-1*heap[0])

'''
OUTPUT:
120 98 100 70  
120
200
100 98 70  
100

'''

