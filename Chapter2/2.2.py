from prettytable import PrettyTable as pt

''' 
    Fixed point iteration Algorithm - page 45,46 - Algorithm 2.2
    Entry values:
        function = f
        Initial aproximation = p0
        Tolerance = TOL
        Max number of iterations = N
    Ouput:
        Approximation result of p or message of failure
'''

# ============================================================================ #
#                        Fixed point iteration Algorithm                       #
# ============================================================================ #

def fixed_point(f, p0, TOL, N):
    try:
    # Configuration for prettytable
        tb = pt()
        tb.align = "l"
        tb.field_names = ["i","p0"]

    # Step 1
        i = 1
    # End Step 1

    # Step 2
        while i <= N:

        # Step 3
            p = f(p0)
            # print(p)
        # End Step 3
            tb.add_row([i,p0])

            # print(np.float32(abs(p-p0)))
        # Step 4
            if (abs(p - p0) < TOL):
                return (
                    print(tb),
                    print(f'\np={p}')
                )
        # End Step 4

        # Step 5
            i += 1
        # End Step 5

        # Step 6
            p0 = p
        # End Step 6

    # End Step 2

    # Step 7
        return print(f'\nEl método fracasó después de {N} iteraciones')
    # End Step 7

    except OverflowError:
        return print(f'\nNo converge')
    

# ============================================================================ #
#                      End Fixed point iteration Algorithm                     #
# ============================================================================ #





# ============================================================================ #
#                            Test Cases                                        #
# ============================================================================ #

# Test Case 1
print("\n\nTest 1")
# f = lambda x: x**3 + 4*x**2 - 10
g = lambda x: 1/2*(10 - x**3)**(1/2)
p0 = 1.5
TOL = 10**-3
N = 100
fixed_point(g, p0, TOL, N)

# Test Case 2
print("\n\nTest 2")
# f = lambda x: x**3 + 4*x**2 - 10
g = lambda x: (10/(4+x))**(1/2)
p0 = 1.5
TOL = 10**-3
N = 100
fixed_point(g, p0, TOL, N)

# ============================================================================ #
#                            End Test Cases                                    #
# ============================================================================ #