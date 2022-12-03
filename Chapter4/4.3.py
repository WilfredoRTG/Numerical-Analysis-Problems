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
#                          Adaptable cuadrant Algorithm                        #
# ============================================================================ #

def AdaptableCuadrant(a,b,TOL,N, f):
    a2 = [0]
    h = [0]
    TOLA = [0]
    FA = [0]
    FB = [0]
    FC = [0]
    S = [0]
    L = [0]

    APP=0
    i=1
    TOLA.insert(i,10*TOL)
    a2.insert(i,a)
    h.insert(i,(b-a)/2)

    FA.insert(i,(a))
    FC.insert(i,f(a+h[i]))
    FB.insert(i,f(b))
    S.insert(i,h[i]*(FA[i]+4*FC[i]+FB[i])/3)

    L.insert(i,1)

    if (i>0):
        FD=f(a2[i]+h[i]/2)
        FE=f(a2[i]+3*h[i]/2)
        S1=h[i]*(FA[i]+4*FD+FC[i])/6
        S2=h[i]*(FC[i]+4*FE+FB[i])/6
        v1=a2[i]
        v2=FA[i]
        v3=FC[i]
        v4=FB[i]
        v5=h[i]
        v6=TOLA[i]
        v7=S[i]
        v8=L[i]
        
        i = i-1

        if(abs(S1+S2-v7)<v6):
            APP=APP+(S1+S2)
            if(v8>=N):
                return ("Nivel Excedido")
            else:
                i=i+1
                a2.insert(i,v1+v5)
                FA.insert(i,v3)
                FC.insert(i,FE)
                FB.insert(i,v4)
                h.insert(i,v5/2)
                TOLA.insert(i,v6/2)
                S.insert(i,S2)
                L.insert(i,v8+1)

                i=i+1
                a2.insert(i,v1)
                FA.insert(i,v2)
                FC.insert(i,FD)
                FB.insert(i,v3)
                h.insert(i,h[i-1])
                TOLA.insert(i,TOLA[i-1])
                S.insert(i,S1)
                L.insert(i,L[i-1])
        return (APP)

# ============================================================================ #
#                    End Adaptable cuadrant Algorithm                          #
# ============================================================================ #




# ============================================================================ #
#                            Test Cases                                        #
# ============================================================================ #

# Test Case 1
a = -1
b = 1
TOL = 1e-12
N = 51
# f = lambda x: (100/x**2)*np.sin(10/x)
f = lambda x: x**2 + x + 1
print(AdaptableCuadrant(a,b,TOL,N, f))

# ============================================================================ #
#                            End Test Cases                                    #
# ============================================================================ #