import heapq

def make_link(G,n1,n2,w):
  if n1 not in G:
    G[n1]={}
  if n2 not in G:
    G[n2]= {}
  G[n1][n2]=w
  G[n2][n1]=w

def initialize_single_source(G,s):
  for v in G:
    G[v]['dist']= float('inf')
    G[v]['parent']=None
  G[s]['dist']=0

def relax(G,u,v,Q):
  if G[v]['dist']> G[u]['dist']+ G[u][v]:
    G[v]['dist']=G[u]['dist']+ G[u][v]
    G[v]['parent'] = u 
    i=0
    for (weight, vertex) in Q:
      if vertex==v:
        Q[i]=(G[v]['dist'],v)
        heapq.heapify(Q)
        break
      i+=1

def dijkstra(G,s):
  initialize_single_source(G,s)
  s = set()
  Q=[]
  for v in G:
    heapq.heappush(Q, (G[v]['dist'],v))

  while len(Q)!= 0:  
    (w,u) = heapq.heappop(Q)
    s = s.union(u)
    for v in G[u]:
      if v not in ('parent', 'dist'):
        relax(G,u,v,Q)



nodes =[(('a','b'),1), (('a','c'),6),(('b','c'),3), (('b','f'),2), (('b','d'),4), (('d','c'),2), (('e','c'),4), (('f','c'),7), (('d','e'),3), (('d','f'),1), (('e','f'),5)]
G={}
for ((n1,n2),w) in nodes:
  make_link(G, n1,n2,w)

#print(G)

#MST_prim(G, 'a')
dijkstra(G,'a')
print()
print()
print(G)
