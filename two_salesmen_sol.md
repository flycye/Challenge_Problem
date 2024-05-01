## Two Traveling Salesmen Problem

### *problem description*

For this problem, you do not need to write a C++ program.


Let G be a weighted acyclic directed graph, with a designated ”start” node, **s** and terminal node **t**. You
wish to find two (directed) paths, each starting at s and ending at t, such that every vertex of **G** is on at
least one of the two paths. The cost of a solution is the sum of the weights of the edges of the two paths.
Design a dynamic programming algorithm that finds a solution of minimum cost, or which finds that no
solution is possible. Remember: a path can’t backtrack.


> e.g.
>
> The figure below shows a weighted directed graph and a solution. The two paths are colored red and blue,
respectively, and each has cost 29. That’s a coincidence; the costs of the two paths can be different. In the
example, the paths meet only at s and t. But they may meet at any vertex.

![Alt text](image.png)

---


### *pseudocode*

> note 1.
> consider minT ⊂ S L(T) + L(S∖T) from source:
> 
> https://math.stackexchange.com/questions/2489528/traveling-salesman-problem-with-two-salesmen
>

1. Write the vertices in topological order (give vertices numerical names)
2. n <- number of vertices
3. array C of size n stores minimum cost for each vertex from s
   1. C(s) = 0
   2. C(i) = infinity
4. Loop over vertices in topological order
   1. for each vertex i
      1. loop over all incoming edges (i, j):
         1. update C(i) = min(C(i), C(j) + w(i, j))
      2. loop over all outgoing edges (k, i):
         1. update C(i) = min(C(i), C(k) + w(k, i))
5. If C(t) = infinity no soln
6. Else
   1. print minimum cost to reach t, C(t)
   2. remember that a path can't backtrack!
7. n <- number of vertices
8. min_cost <- set to inf
9. divide the vertices into two sets from s to t
   1.  loop through each partition and calculate the minimum costs
   2.  for every starting node in both partitions, set the minimum cost
10. if the minimum cost is infinite, no soln
11. else
    1.  return the minimum cost

> Remember that sorting something topologically means
> arranging the nodes of a DAG in a way for every 
> directed edge u --> v, node u comes before node v in ordering
>
> This can be done using a Depth-First Search.

---
