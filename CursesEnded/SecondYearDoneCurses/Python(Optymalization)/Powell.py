import numpy as np
from scipy.optimize import bracket
from scipy.optimize import minimize


def powell(F, x, h=0.1, tol=1.0e-0):

    def f(s): return F(x + s*v) # F in direction of v

    n = len(x)                # Humber of design variables
    df = np.zeros(n)          # Decreases of F stored here
    u = np.identity(n)        # Vectors v stored here by rows
    for j in range(30):       # Allow for 30 cycles:
       xOld = x.copy()        # Save starting point
       fOld = F(xOld)
     # First n live searches record decreases of F
        for i in range(n):
            v = u[i]
            a, b = bracket(f, 0.0, h)
            s, fMin = search(f,a,b)
          df[1] = fOld -tUft
          fOld =
          x = x + a*v
       Last 1.e sear. . the cycle

       a,b = bracket(f.O.O.h)
       s,frast = search(f,a,b)

       Check for convergence
       If Math. grt(r.p.dot(x-xOld.x-x01d)/n) < tol: recur])
       /dentify biggest decrease update seamen directions
          = np.argmax(df)
       for i   range(1Max.n-1):
          u[i] -1(1+1]
       III 1] = v
    print( "Powell did not converge)
