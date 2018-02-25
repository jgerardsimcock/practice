'''
Recursive functions, dynamic programming and memoization. 

The process of breaking larger problems into smaller subproblems

'''

class Fibb:


    def __init__(self):
        self.memo = {}


    def fib(self, n):

        #catches user input error?
        if n < 0:
            raise Exception('Index was negative')

        #catches case where we recurse to
        #end of problem
        elif n in [0,1]:


        if n in self.memo:
            print("we've computed this input. Obtaining value memo")
            return self.memo[n]

        print("new input. Let's compute")
        
        result = self.fib(n - 1) + self.fib(n -2)

        self.memo[n] = result

        return result