def f(x):
    return x**3 - 2*x**2 - 5

def bisection_method(a, b, f, n_decimals):
    """Finds the root of a function f within the interval [a, b] using the bisection method
    and rounds the result to n_decimals decimal places."""

    # Calculate the midpoint of the interval
    c = (a + b) / 2.0
    
    # Check if the midpoint is already the root
    if round(f(c), n_decimals) == 0:
        return round(c, n_decimals)
    
    # Repeat until the interval is small enough
    while round(b - a, n_decimals) > 0:
        # Evaluate the function at the midpoint
        f_c = f(c)
        
        # Determine which half of the interval to keep
        if round(f_c, n_decimals) * round(f(a), n_decimals) < 0:
            b = c
        else:
            a = c
        
        # Calculate the new midpoint
        c = (a + b) / 2.0
        
        # Check if the new midpoint is the root
        if round(f(c), n_decimals) == 0:
            return round(c, n_decimals)
    # Return the midpoint of the final interval
    return round(c, n_decimals)

root = bisection_method(1, 3, f, 4)
print("The root of the function is:", root)