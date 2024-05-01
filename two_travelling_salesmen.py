from collections import defaultdict


# function to topologically sort a graph of nodes, with source node
# ensures no cycles are encountered
def topological_sort(graph):
    visited = set()     # create a set to keep track of visited nodes
    stack = []          # create a stack to push nodes in topological order

    # perform a depth-first search traversal from starting node 'node'
    def dfs(node):
        visited.add(node)   # add the current node as visited

        # for each of its neighbours . . .
        for neighbour in graph[node]:

            # if the neighbour is not visited, perform dfs
            if neighbour not in visited:
                dfs(neighbour)
        stack.append(node)  # once all neighbours visited, append to stack

    # for all unvisited nodes, perform DFS search above
    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]      # nodes topologically sorted in reverse order

# find the minimum cost (brute-force)
def find_min_cost(graph, weights, s, t):

    # create an array C of size n that stores min cost
    # for each vertex from source, setting C(i) to inf
    C  = defaultdict(lambda: float("inf"))

    C[s] = 0    # set cost of source node to zero

    # topologically sort the graph of nodes
    top_sort = topological_sort(graph)

    # iterate through the nodes in topological order

    for node in top_sort:
        # for each node, iterate through its neighbours
        for neighbour in graph[node]:
            # update min(C(i), C(k) + w(k, i))
            C[node] = min(C[node], C[neighbour] + weights[(neighbour, node)])
        for neighbour in graph[node]:
            if node in graph[neighbour]:
                # update min(C(i), C(k) + w(k, i))
                C[node] = min(C[node], C[neighbour] + weights[(neighbour, node)])
   
    # if C(t) == infinity, no soln. else backtrack to find path & print
    if C[t] == float("inf"):
        return "no solution"
    else:
        return C[t]
        
# solve the two travelling salesmen problem using the funcs created above
def two_traveling_salesmen(graph, weights, s, t):
    min_cost = float("inf")     # minimum cost set to inf
    n = len(graph)              # store the length of the graph

    # iterate through all divisions of vertices into two sets
    for i in range(1, 2 ** (n - 1)):
        # divide the vertices into two sets. paths must start from s 
        # and end at t
        firstPartition = []
        secondPartition = []

        # for each partition, calculate the minimum cost
        # from the vertex
        for j in range(n):
            if (i >> j) & 1:
                firstPartition.append(j)
            else:
                secondPartition.append(j)

        # ensure source and target are in different sets
        if s in firstPartition and secondPartition:
            cost1 = find_min_cost(graph, weights, s, firstPartition[0])
            cost2 = find_min_cost(graph, weights, t, secondPartition[0])

            # set minimum score to minimum of partitions costs
            # and minimum cost found
            min_cost = min(min_cost, cost1 + cost2)
    
    # if the minimum cost is infinite, no minimum cost was found
    # therefore there is no solution
    if min_cost == float("inf"):
        return "no solution"
    else:
        return min_cost     # otherwise, return the minimum cost found