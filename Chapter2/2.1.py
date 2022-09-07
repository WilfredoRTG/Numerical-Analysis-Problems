from prettytable import PrettyTable as pt
''' 
    Bisection Algorithm - page 37 - Algorithm 2.1
    Entry values:
        Final value a = a
        Final value b = b
        Tolerance = TOL
        Max number of iterations = N
    Ouput:
        Approximation result of p or message of failure
'''

# ============================================================================ #
#                              Bisection Algorithm                             #
# ============================================================================ #
def bisection(f, a, b, TOL, N):
    # Configuration for prettytable
    tb = pt()
    tb.align = "l"
    tb.field_names = ["n","an", "bn","pn","f(pn)"]

# Step 1
    i = 1
    FA = f(a)
# End Step 1

# Step 2
    while i <= N:
    # Step 3
        p = a + (b - a) / 2
        FP = f(p)
    # End Step 3
        tb.add_row([i,a,b,p,FP])

    # Step 4
        if (FP == 0) or ((b - a) / 2 < TOL):
            return (
                print(tb),
                print(f'\np={p}')
            )
    # End Step 4
    
    # Step 5
        i += 1
    # End Step 5
    # Step 6
        if FA*FP > 0:
            a = p
            FA = FP
        else:
            b = p
    # End Step 6

# End Step 2

# Step 7
    return print(f'\nEl método fracasó después de {N} iteraciones')
# End Step 7

# ============================================================================ #
#                            End Bisection Algorithm                           #
# ============================================================================ #





# ============================================================================ #
#                            Test Cases                                        #
# ============================================================================ #

# Test Case 1
print("\n\nTest 1")
f = lambda x: x**3 + 4*x**2 - 10
a = 0
b = 5
TOL = 10**-3
N = 100
bisection(f, a, b, TOL, N)

# Test Case 2
print("\n\nTest 2")
f = lambda x:  4*x**2 - x - 10
a = 0
b = 5
TOL = 10**-6
N = 100
bisection(f, a, b, TOL, N)

# ============================================================================ #
#                            End Test Cases                                    #
# ============================================================================ #