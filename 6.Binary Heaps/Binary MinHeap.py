'''
Implementation of Binary Min Heap using heapq module..
By default this module will give min Heap.
'''
import heapq as h
heap=[]
h.heapify(heap)
def printheap(heap):
    for i in heap:
        print(i,end=' ')
    print(" ")

#insert
h.heappush(heap,100)
h.heappush(heap,98)
h.heappush(heap,120)
h.heappush(heap,70)
#print
printheap(heap)
print(h.heappop(heap)) #pop min element
print(h.heappushpop(heap,200))
printheap(heap)
print(heap[0])
'''
OUTPUT:
70 98 120 100  
70
98
100 200 120  
100

'''


