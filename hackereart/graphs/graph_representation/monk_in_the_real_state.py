#not necessary
def make_link(G, n1, n2):
    if n1 not in G:
        G[n1]={}
    G[n1][n2]= 1
    if n2 not in G:
        G[n2]= {}
    G[n2][n1]=1
    return G


# Write your code here
T = int(input())
for i in range(T):
    ##for cada test
    G={}
    E = int(input())
    s = set()
    for j in range(E):
        node1, node2 = map(int, input().split())
        s.add(node1)
        s.add(node2)
        #make_link(G,node1,node2)
    print(len(s))
        
