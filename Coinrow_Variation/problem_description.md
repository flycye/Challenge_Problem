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



---


## *code*

### function to find the max coin value
### without three consecutive coins (pos)


      def maxCoinValue(coins):
         n = len(coins)

         if n == 0: return 0
         if n == 1: return coins[0]

         maxValues = [0] * n
         maxValues[1] = max(coins[0], coins[1])

         for i in range(2, n):
            maxValues[i] = max(maxValues[i - 2] + coins[i], maxValues[i - 1])

         return maxValues[n]

      coins = [5, 1, 2, 10, 6, 2]
      print("max coin value: ", maxCoinValue(coins))

---

## done!
