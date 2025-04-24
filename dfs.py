graph={
    "a":["b","c"],
    "b":["d"],
    "c":[],
    "d":[]
}
def dfs(node):
    print(node)
    for i in graph[node]:
        dfs(i)
dfs("a")
