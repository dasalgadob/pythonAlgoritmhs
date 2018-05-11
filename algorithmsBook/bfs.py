from collections import deque


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G
    
edges1 = [('v', 'r'), ('r', 's'), ('w', 't'), ('s','w'),
         ('w', 'x'), ('t', 'x'), ('t', 'u'), ('x', 'y'),
         ('u', 'y')]

G1 = {'y':{}}
for v1, v2 in edges1:
    make_link(G1, v1, v2)

#print (G1)

#G1['y']['color']= "black"
#print(G1)

def bfs(G,s):
  for node in G.keys():
    G[node]['color'] = "white"
    G[node]['d'] = -1
    G[node]['parent']= None
  G[s]['color'] = 'grey'
  G[s]['d']=0
  G[s]['parent']=None
  #print(G)
  q = deque()
  q.append(s)
  while len(q) != 0:
    e =q.popleft()
    for n in G[e].keys():
      if n =='color' or n== 'd' or n=='parent':
        continue
      if G[n]['color']== 'white':
        G[n]['color'] = 'grey'
        G[n]['d'] =  G[e]['d']+1
        G[n]['parent']= e
        q.append(n)
    G[e]['color']='black'
    
bfs(G1,'u')

print(G1)

def print_path(G,s,v):
  if v == s:
    print(s, end=' ')
  elif G[v]['parent'] == None:
    print("No path")
  else:
    print_path(G,s, G[v]['parent'])
    print(v, end=' ')
    
print_path(G1,'u','s')
