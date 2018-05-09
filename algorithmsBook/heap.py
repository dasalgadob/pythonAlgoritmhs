L = [16,14,10,8,7,9,3,4,1]

class Heap:
  def parent(self, i):
    return int((i-1)/2)
  
  def left(self, i):  
    return int(i*2+1)
   
  def right(self, i):  
    return int(i*2+2)  
    
h = Heap()
#print(h.parent(8))
#print(h.parent(7))
  
#print(h.left(2))  
#print(h.right(2))  

def max_heapify(A,i,heap):
  l = heap.left(i)
  r = heap.right(i)
  #print("r:"+ str(r))
  if l < len(A) and  A[l]>A[i]:
    largest = l
  else:
    largest = i
  if r < len(A) and A[r]>A[largest] :
    largest =r
  if largest != i:
    temp = A[i]
    A[i] = A[largest]
    A[largest] = temp
    max_heapify(A,largest,heap)
    
L[0] = 2
max_heapify(L, 0, h)
print(L)

def build_max_heap(A,heap):
  print(heap.parent(len(A)-1))
  for i in range(heap.parent(len(A)-1),-1,-1):
    print("i:"+ str(i))
    max_heapify(A,i,heap)
    print(A)
    
A= [4,1,3,2,16,9,10,14,8,7]
build_max_heap(A,h)
print(A)

    
