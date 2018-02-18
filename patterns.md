patterns
--------


Greedy: Routines that set an initial value to be updated when new information arrives
        This question relies on understanding what initial value to store.


Routines that increment a value at every pass


Routines that solve problems by splitting the search space in two and evaluating 

Routines that splite the problem in two and then sum (map, reduce)

Brute Force: try all possible solutions and check for correctness. 




Notes on Big O
--------------

Big-O is the expression of the efficiency of an algorithm. Express runtime in relation to how quickly it grows wrt inputs, as the inputs get larger.

Speed and efficiency of an algorithm are relative to the input n

Big-O also referred to as asymtotic analysis

O(1) is constant time relative to input: a function requires a single step regardless of input

O(n) is linear time. As n grows so does the time to compute. It scales linearly as inputs scale

O(n^2) is quadratic time. This is where for every input we must do an operation n*n times. 


Space Complexity and Big-O
--------------------------

O(1) constant space time is a fixed number of variables 



Data Structures
---------------

Arrays
======

* In python arrays are called lists
* ordered collection of elements
* efficient for looking up an element at an index
* lookup time is O(1) 
* Foundation for other data structures like: stacks, hash tables, and dynamic arrays
* In python, lists are dynamic arrays. You do not need to specify the size of the array a priori. You can insert and delete elements at any index in the list. 
* Strings are implemented as arrays of characters. 


Hash tables
===========
* dictionaries, hash map, map, unordered map, hash are synonyms depending on language
* insertion and look up are constant O(1) time 
* In python this is a dictionary.
* Unordered, can be varied data types
* Similar to an array if you think of array indexes as keys
* Hash Collisions: two different inputs generate the same output.
* Hash Rebalancing



