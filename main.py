def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)

    
      
    
def fib_top_down(n, fibs):
    ###TODO
    if fibs[n] != -1:
      return fibs[n]
    elif n <= 1:
      return n
    else:
      return fib_top_down(n-1, fibs) + fib_top_down(n-2, fibs)


def fib_bottom_up(n):
    ###TODO
    if n <= 1:
      return n
    fib = [0] *(n+1)
    fib[1] = 1
    for i in range(2, n+1):
      fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
