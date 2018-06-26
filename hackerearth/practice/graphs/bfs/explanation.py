
from collections import deque 

def make_link(G,node1,node2):
    if node1 not in G:
        G[node1]={}
    G[node1][node2]=1
    if node2 not in G:
        G[node2]={}
    G[node2][node1]= 1
    
##It just going to make bfs until the level x that is passed
def bfs(G,s):
    for n in G.keys():
        G[n]['d']=-1
        G[n]['c']="white"
        G[n]['p']=None
    G[s]['d']=0
    G[s]['c']="grey"
    G[s]['p']=None
    q = deque()
    
    q.append(s)
    while len(q) != 0:
        e = q.popleft()
        ##Si distancia mayor a la buscada terminar
        for n in G[e].keys():
            if n in ("c","p","d"):
                continue
            if G[n]['c']=="white":
                G[n]['d']= G[e]['d']+1
                G[n]['p']=e
                G[n]['c']="grey"
                q.append(n)
        G[e]['c']="black"
                

# Write your code here
N = int(input())
G={}
for i in range(N-1):
    a,b = [int(i) for i in input().split()]
    make_link(G,a,b)
x= int(input())
##Contar cuantos estan a distancia 

if N==1 and x==0:
    print(1)
else:
    bfs(G,1)
    count=0
    for n in G.keys():
        if G[n]['d']==x-1:
            count+=1
    print(count)
#print(G)    
