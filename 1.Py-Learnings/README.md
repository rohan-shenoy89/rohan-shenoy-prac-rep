** ALGORITHMIC COMPLEXITY - NOTES **

Important factors to consider the complexity
    a. TIME
    b. SPACE

TECHNIQUES:
    1. Measuring Time to execute --> This can differ based on the Machine config --> REJECTED
    2. Counting Operations involved --> Time changes with the change in operation --> REJECTED
    3. Abstract notion of order of growth --> Industry accepted approach.


BASICS TO GET THE BIG O NOTATION:
    1.  Count the number of operation
    2.  Check the loops and see the number of operations
        a. If you want to check or get the number of operation then:
        
            1: Consider there is 1 operation outside the loop
            5n: There are 5 operations inside the loop
            
            Formula - 1 + 5n

            Cal Rule :
                a. Remove the additive/constant operation. i.e. remove 1 from above formula.
                        Reminder: 5n
                b. Remove the multiplicative operations i.e. remove 5 from the formula.
                        Reminder: n
                c. Remove the small factor from the formula, if any. For example if there is n2 + n, then
                    you remove n from the formula.
                d. 

            Output: O(n) --> Linear Operation

O notaion details:
    a. O(n)       --> Linear Operation (This will grow in the case of values that grows.)
    b. O(n2)      --> Quadratic Operation (Nested loop or Bubble sort are mostly quadratic)
    c. O(nlog(n)) --> n Log n (Merge sort or quick sort is example of n log n)
    d. O(1)       --> Constant (This will remain constant in case of Index search)
    e. O(log(n))  --> Logarithmic Operation (The time is incremented by number each time the input is multiplied by number. Binary search is an example of lograthmic)
    f. O(bn)      --> Exponential Operation (This is straight opposite to logarithmic)

NOTE: 
    1. If there is (n)^2 that means its a "Nested Loop"
    2. If there is 2n that means there are "2 operations inside Loop"
    3. If there is single value like 2 that means there "is simple operation" outside loop.
                
            
