To understand the mathematics involved there are a number of pre-requisites.
One needs to know:

 * What is a group of permutations and some knowledge of group theory, like:
   * What are the cyclic groups.
   * What is a Cartesian product of groups
   * What is the cycle decomposition/factorization of the elements of a group of permutations.
 * The definition of the cycle index polynomial, how to compute it and some properties like:
  * How the cycle index polynomial of a cyclic group looks like.
  * How the cycle index polynomial of a Cartesian product of groups depends on the cycle index polynomials of the groups that are being multiplied.

In the problem the collection of all matrices are grouped into [equivalence classes](https://en.wikipedia.org/wiki/Equivalence_class)
according to the action of a [group of permutation](https://en.wikipedia.org/wiki/Permutation_group).

[Polya enumeration theorem](https://en.wikipedia.org/wiki/Permutation_group) is just a theorem that tells the number of those classes by means of a formula.
The formula is expressed in terms of a polynomial that is computed from the group of permutations. In particular from the cycle factorizations of the elements of the group.
This polynomial is called the cycle index polynomial of the group.

A book that talks a good deal about Polya's enumeration theorem and other results related to it is

    Harary and Palmer's Graphical enumeration, Chapter 2.

An article that has a formula to compute the cycle index polynomial of a group that is a Cartesian product of two other groups is

  Cycle index of direct product of permutation groups and number of equivalence classes of subsets of Z_n, Wan-Di Wei  and Ju-Yong Xu (1993)

After using the formulas you get the expression at the end of https://franklinvp.github.io/2020-06-05-PolyaFooBar/
Then it is just a matter of computing that sum with all those factorials, greater common divisors, and partitions of a number.

[StackOverflow explaining](https://stackoverflow.com/questions/61689832/disorderly-escape-google-foobar-2020-not-passing-test-cases)
