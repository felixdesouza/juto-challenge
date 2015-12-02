# juto-challenge

Very rough impl, no checking or deduplication, more of just experimenting/trying to get it running.

Idea is:
  - compute f(5 * 10^6) which is some large BigInteger, do this using matrices. See Matrix class.
  - since we're doing f(N) mod M where N >>>>> M, we can mod the intermediate results too. See ModMatrix class

Given Matrix A: 
```
0 1 0
0 0 1
2 0 1
```
Can work out f(n) by calculating e_1^T * A^n e_3 

where e_i are the standard 3 column vectors

or simply A_{0,2}

Can do the squaring in log(n) so really, calculating f(5 * 10^6) happens in 22 or so steps of matrix mult, as opposed to 5 * 10^6 steps

Possible alternate solution?

 - Having to compute f(5 * 10^6) isn't too slow, but since we're working mod M, perhaps there is a cycle as any 4 consecutive numbers fix the order
 - **If** there is a cycle, then we needn't compute the large number by f(5 * 10 ^ 6), we can use ModMatrix **again**, but with a modulo of the cycle length
 - After that can use ModMatrix again with the result above, but with modulo 10^9 and should arrive at the same answer.
