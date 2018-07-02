import heapq

def make_link(G,n1,n2,w):
  if n1 not in G:
    G[n1]={}
  if n2 not in G:
    G[n2]= {}
  G[n1][n2]=w
  G[n2][n1]=w

def MST_prim(G, r):
  Q = []
  for v in G:
    G[v]['key']=float('inf')
    G[v]['parent']=None
  G[r]['key']=0
  for v in G:
    heapq.heappush(Q, (G[v]['key'],v))
  
  while len(Q)!= 0:
    (peso, e) = heapq.heappop(Q)
    print((e,G[e]))
    for v in G[e]:
      if v not in ('key','parent') and (G[v]['key'],v) in Q and G[e][v]<G[v]['key']:
        G[v]['parent']= e
        G[v]['key']=G[v][e]
        i=0
        for (weight, vertex) in Q:
          if vertex==v:
            Q[i]=(G[v][e],v)
            heapq.heapify(Q)
            break
          i+=1


nodes =[(('a','b'),1), (('a','c'),6),(('b','c'),3), (('b','f'),2), (('b','d'),4), (('d','c'),2), (('e','c'),4), (('f','c'),7), (('d','e'),3), (('d','f'),1), (('e','f'),5)]
G={}
for ((n1,n2),w) in nodes:
  make_link(G, n1,n2,w)

#print(G)

MST_prim(G, 'a')
print()
print()
print(G)
