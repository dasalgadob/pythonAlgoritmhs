
def make_link(G,n1,n2):
    if n1 not in G:
      G[n1]={}
    G[n1][n2]=1
    if n2 not in G:
      G[n2]={}
    G[n2][n1]=1

def dfsModified(G,s):
    for n in G:
        G[n]['c']="w"
        G[n]['p']=None
    dfs_visit(G,s)
    c =0
    for n in G:
        if G[n]['c']=="w":
            c+=1
            #print(n)
    return c
    
def dfs_visit(G,s):
    G[s]['c']="g"
    for n in G[s]:
        if n not in ('c','p') and G[n]['c']=="w":
            G[n]['c']='g'
            G[n]['p']=s
            dfs_visit(G,n)
    G[s]['c']='b'
    
        
    
    
N, M= map(int, input().split())
G={}
for i in range(1,N+1):
  G[i]={}
for i in range(M):
    a,b = map(int, input().split())
    #print((a,b))
    make_link(G,a,b)


#print(len(G))
s = int(input())
c = dfsModified(G,s)
#print(G)
print(c)
