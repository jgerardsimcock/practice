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


Amortized Analysis
==================

Look at the cost of a single expensive operation, over the long-run cost of a large number of cheap operations





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

Dynamic Arrays
==============

* Array will grow if you try to make insertion and there is not enough space
* Under the hood, all the elements of the array are copied to a new larger array
* This operation, performs a copy operation on every element of the smaller array resulting in a linear runtime of O(n)
* However, most insert operations are constant
* We create frequent cheap constant time insertions at the cost of expensive infrequent linear time insertions.


Hash tables
===========
* dictionaries, hash map, map, unordered map, hash are synonyms depending on language
* insertion and look up are constant O(1) time 
* In python this is a dictionary.
* Unordered, can be varied data types
* Similar to an array if you think of array indexes as keys
* Hash Collisions: two different inputs generate the same output.
* Hash Rebalancing

Linked Lists
============

* Only reference point to the linked-list is the head node
* All subordinate values in the list link back to the head/root node
* Constant time O(1) insertions and deletions
* Lookups on linked-lists are take O(i) to go from head to ith value in list
* Edits and lookups must move from head to ith item

Doubly Linked Lists
===================

* Pointers to next and previous node of the list
* Allow user to traverse the forwards and backwards

Call Stack
----------

What a program uses to keep track of what function is currently running and what to do with that functions return value.

When you call a function, a new frame gets pushed onto the call stack, which then gets popped when the function returns. As functions call other functions, the stack gets taller. In recursive functions, the stack gets as tall as the number of times the function calls itself. 

If the stack gets too big, a stack overflow error can occur. 

Concurrency
===========

Concurrency models


Problems and Subproblems
========================

Divide and conquer is an effective strategy for thinking about problem solving. 


Recursion and Memoization
-------------------------

Given an input we can store results of a computation's output. This allows us to not rerun on a computation for a given input. This is useful in recursion, where we frequently will have common inputs into a computation. As we break problems into subproblems the possibility for recursion increases and the utility of memoization becomes more apparent for saving compute time. 

In practice, this is simply using some datastructure to save outputs for given inputs and if we find ourselves using the same input again we can just lookup the data structure
value instead of doing the computation.


Dynamic Programming and subproblems
-----------------------------------


Bottom-up
---------


