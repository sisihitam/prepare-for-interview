# Knapsack Problem
## Traditional thinking
In the following recursion tree, K() refers 
to knapSack(). The two parameters indicated in the
following recursion tree are n and W.
The recursion tree is for following sample inputs.
```
wt[] = {1, 1, 1}, W = 2, val[] = {10, 20, 30}
```
```
                       K(n, W)
                       K(3, 2)  
                   /            \ 
                 /                \               
            K(2, 2)                  K(2, 1)
          /       \                  /    \ 
        /           \              /        \
       K(1, 2)      K(1, 1)        K(1, 1)     K(1, 0)
       /  \         /   \          /   \
     /      \     /       \      /       \
K(0, 2)  K(0, 1)  K(0, 1)  K(0, 0)  K(0, 1)   K(0, 0)
```
Recursion tree for Knapsack capacity 2 
units and 3 items of 1 unit weight.

## Complexity Analysis:

Time Complexity: `O(2^n)`.
As there are redundant subproblems.
Auxiliary Space :`O(1)`.
As no extra data structure has been used for storing values.