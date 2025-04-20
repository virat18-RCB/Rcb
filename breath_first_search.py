graph={
    "a":["b","c"],
    "b":["d"],
    "c":["e"],
    "d":[],
    "e":[]
}
v=[]
q=[]
s="a"
q.append(s)
while q:
    node=q.pop(0)
    if node not in v:
        v.append(node)
        q+=graph[node]
print(v)
