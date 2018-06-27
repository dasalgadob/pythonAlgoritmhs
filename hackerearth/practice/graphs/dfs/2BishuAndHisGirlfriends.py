N= int(input())
G={}
from  collections import deque
def make_link(G,n1,n2):
    if n1 not in G:
        G[n1]={}
    G[n1][n2]= 1
    if n2 not in G:
        G[n2]={}
    G[n2][n1]=1
    
def bfs(G,s):
    for n in G:
        G[n]['c']="w"
        G[n]['p']=None
        G[n]['d'] = -1
    G[s]['c']="g"
    G[s]['d']=0
    q= deque()
    q.appendleft(s)
    while len(q) != 0:
        e = q.pop()
    for n in G[e]:
        if n not in ('c', 'p', 'd') and G[n]['c']=="w":
            G[n]['d']=G[e]['d']+1
            G[n]['p']= e
            G[n]['c']= "g"
            q.appendleft(e)
        G[e]['c']="b"
            

for i in range(N-1):
    a,b= map(int, input().split())
    make_link(G,a,b)
bfs(G,1)
Q = int(input())
girl=[]
for i in range(Q):
    girl.append((0,int(input())))
girl.sort()
print(girl[0][1])
    
