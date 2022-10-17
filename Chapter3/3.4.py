from prettytable import PrettyTable as pt

''' 
    Natural Cubic Spline Algorithm - page 110 - Algorithm 3.4
    Entry values:
        function = f
        Initial aproximation = p0
        Tolerance = TOL
        Max number of iterations = N
    Ouput:
        Approximation result of p or message of failure
'''

# ============================================================================ #
#                      Natural Cubic Spline Algorithm                          #
# ============================================================================ #

def Spline(valX, an):
    h = []
    for i in range(len(valX)-1):
        h.append(valX[i+1]-valX[i])
    al=[]
    for i in range(1,len(valX)-1):
        s1 = 3*(an[i+1]-an[i])/h[i]
        s2 = 3*(an[i]-an[i-1])/h[i-1]
        al.append((s1-s2))
    l0 = 1
    m0 = 0
    z0 = 0
    l = [l0]
    m = [m0]
    z = [z0]
    for i in range(len(valX)-1):
        li = 2*(valX[i+1]-valX[i-1])-h[i-1]*m[i-1]
        l.append(li)
        mi = h[i]/li
        m.append(mi)
        zi = (al[i-1]-h[i-1]*z[i-1])/li
        z.append(zi)
    
    l.insert(len(valX), 1)
    z.insert(len(valX), 0)
    cj = []
    bj = []
    dj = []
    for i in range(len(valX)):
        cj.append(0)
        bj.append(0)
        dj.append(0)

    for j in range(len(valX)-2,-1,-1):
        cj[j] = z[j]-m[j]*cj[j+1]
        bj[j] = (an[j+1]-an[j])/h[j]-h[j]*(cj[j+1]+2*cj[j])/3
        dj[j] = (cj[j+1]-cj[j])/(3*h[j])        


    return an, bj, cj, dj

# ============================================================================ #
#                    End Natural Cubic Spline Algorithm                        #
# ============================================================================ #




# ============================================================================ #
#                            Test Cases                                        #
# ============================================================================ #

# Test Case 1
print("\n\nTest 1")

valX = [1, 1.3, 1.6, 1.9, 2.2]
an =  [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]


a = Spline(valX, an)
print(a)

# ============================================================================ #
#                            End Test Cases                                    #
# ============================================================================ #