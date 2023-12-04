# CMPS 2200 Recitation 06
## Answers

**Name:** Ali Sulehria 
**Name:**


Place all written answers from `recitation-06.md` here for easier grading.



- **2)**

- The work is W(n) = W(n-1) + W(n-2) + 1. This, being leaf-dominated, is of the order O(2^n).

- **3)**

The span is S(n) = S(n- 3/2) + 1, so it is O(n).

- **4)**

While looking at the counts list, the first term is the second-to-last term of the sequence. The next n values are the fibonacci sequence in reverse.

- **6)**

The maximum # of calls for the top-down method is once, as it only needs to be called once to be put into the list. Because of this, the work and span decrease to O(n) (no parallelism)

- **8)**

For some i, the bottom-up function will be called a maximum of i times for each value. This is still constant and non-recursive, so the work and span are O(n).