import sys
input = sys.stdin.read()
n,k = map(int, input.split())
points = []
for i in range(n):
    points.append([])
for j in range(n-1):
    x,y=map(float,sys.stdin.readline().split())
    points[j].append((x,y))
q=[]
visited=[False]*n
visited[k]=True
q.append(k)
min_length=0
while len(q)>0:
    u=q.pop(0)
    for i in range(len(points)):
        if visited[i]==False and abs(points[u][0]-points[i][0])+abs(points[u][1]-points[i][1])<min_length:
            q.append(i)
            visited[i]=True
            min_length=abs(points[u][0]-points[i][0])+abs(points[u][1]-points[i][1])
print(min_length)
