import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
adj=[[] for _ in range(n+1)]
for i in range(n-1):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)
q=int(input())
output=[]
for _ in range(q):
    v,k=map(int,input().split())
    if len(adj[v])==1:
        output.append(5)
    else:
        deleted=[0]*n
        deleted[v]=1
        while len(deleted)>1:
            for i in range(2,n+1):
                if deleted[i]:
                    continue
                for j in range(2,n+1):
                    if deleted[j]:
                        continue
                    if adj[i][0]==v and adj[j][0]!=v:
                        deleted[j]=1
                        break
        output.append(len(adj[v])-sum(deleted))-k)
print(*output,sep='\n')
