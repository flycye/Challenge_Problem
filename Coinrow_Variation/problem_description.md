# Coin-row Variation Problem

### *problem description*

 Write pseudocode for a dynamic programming problem that solves a variation of the coin-row problem.
All coins have positive value, and the set of coins selected may not contain any three consecutive coins.
This problem is much trickier than the original version where you may not select any two consecutive
coins.


---


### *pseudocode*

> note 1.
> all coin row variation problems are implemented
> using dynamic programming

1. base cases
   1. if there are no coins, there is no coinrow
   2. if there is one coin, the max is the only coin's amount/value
   3. if there are only two coins, return the max value of the two
2. create a list to store the max value for coins up to the **ith** position
3. for the first element, add the first coin's element
4. for the second elements, take the max of the first two element's
5. for all other elements from 2 to n
   1. add the value of the current coin to the value of the coin before previous, if greater than prev
6. return the last element in maxValues (bigger)
