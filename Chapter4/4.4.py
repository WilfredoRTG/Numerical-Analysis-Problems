from prettytable import PrettyTable as pt
import numpy as np
''' 
    Newton Algorithm - page 166 - Algorithm 4.3
    Entry values:
        a,b sides = a, b
        tolerancia = TOL
        Diferentes levels = N
    Ouput:
        Approximation APP or message of success N
'''

# ============================================================================ #
#                     Integral doble de Simpson Algorithm                      #
# ============================================================================ #

def IntegralDoble(a,b,m,n,f, dx, cx):
    h = (b-a)/n
    j1 = 0
    j2 = 0
    j3 = 0

    for i in range(n+1):
        x = a + (i*h)
        HX = (dx(x) - cx(x))/m
        k1 = f(x,cx(x)) + f(x, dx(x))
        k2 = 0
        k3 = 0
        for j in range(1, m):
            y = cx(x) + (j*HX)
            Q = f(x,y)
        
            if j:
                k2 = k2 + Q
                k3 = k3 + Q
        
        L = ((k1 + (2*k2) + (4*k3))*HX)/3

        if i == 0 or i ==n:
            j1 = j1 + L
        elif i:
            j2 = j2 + L
            j3 = j3 + L
        
        J = h*(j1 + (2*j2) + (4*j3))/3

    return J



# ============================================================================ #
#                 End Integral doble de Simpson  Algorithm                     #
# ============================================================================ #




# ============================================================================ #
#                            Test Cases                                        #
# ============================================================================ #

# Test Case 1
a = 0.1
b = 0.5
m = 10
n = 10
# f = lambda x: (100/x**2)*np.sin(10/x)
f = lambda x, y: np.exp(x/y)
dx = lambda x: x**2 
cx = lambda x: x**3
print(IntegralDoble(a,b, m, n, f, dx, cx))

# ============================================================================ #
#                            End Test Cases                                    #
# ============================================================================ #