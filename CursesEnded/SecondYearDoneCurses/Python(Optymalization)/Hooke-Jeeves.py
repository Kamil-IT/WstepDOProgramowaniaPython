import numpy as np


def best_nearby(delta, point, prevbest, nvars, f, funevals):
    # BEST_NEARBY looks for a better nearby point, one coordinate at a time.

    z = point.copy()

    minf = prevbest

    for i in range(0, nvars):

        z[i] = point[i] + delta[i]

        ftmp = f(z, nvars)
        funevals = funevals + 1

        if (ftmp < minf):

            minf = ftmp

        else:

            delta[i] = - delta[i]
            z[i] = point[i] + delta[i]
            ftmp = f(z, nvars)
            funevals = funevals + 1

            if (ftmp < minf):
                minf = ftmp
            else:
                z[i] = point[i]

    point = z.copy()
    newbest = minf

    return newbest, point, funevals


def hooke(nvars, startpt, rho, eps, f):
    # HOOKE seeks a minimizer of a scalar function of several variables.
    #  Parameters:
    #
    #    Input, integer NVARS, the number of spatial dimensions.
    #
    #    Input, real STARTPT(NVARS), the user-supplied
    #    initial estimate for the minimizer.
    #
    #    Input, real RHO, a user-supplied convergence parameter
    #    which should be set to a value between 0.0 and 1.0.  Larger values
    #    of RHO give greater probability of convergence on highly nonlinear
    #    functions, at a cost of more function evaluations.  Smaller
    #    values of RHO reduce the number of evaluations and the program
    #    running time, but increases the risk of nonconvergence.
    #
    #    Input, real EPS, the criterion for halting
    #    the search for a minimum.  When the algorithm
    #    begins to make less and less progress on each
    #    iteration, it checks the halting criterion: if
    #    the stepsize is below EPS, terminate the
    #    iteration and return the current best estimate
    #    of the minimum.  Larger values of EPS (such
    #    as 1.0e-4) give quicker running time, but a
    #    less accurate estimate of the minimum.  Smaller
    #    values of EPS (such as 1.0e-7) give longer
    #    running time, but a more accurate estimate of
    #    the minimum.
    #
    #    Input, function handle F, the name of the function routine,
    #    which should have the form:
    #      function value = f ( x, n )
    #
    #    Output, integer ITERS, the number of iterations taken.
    #
    #    Output, real ENDPT(NVARS), the estimate for the
    #    minimizer, as calculated by the program.
    #

    verbose = False

    newx = startpt.copy()
    xbefore = startpt.copy()

    delta = np.zeros(nvars)

    for i in range(0, nvars):
        if (startpt[i] == 0.0):
            delta[i] = rho
        else:
            delta[i] = rho * abs(startpt[i])

    funevals = 0
    steplength = rho
    iters = 0
    fbefore = f(newx, nvars)
    funevals = funevals + 1
    newf = fbefore

    while eps < steplength:
        iters = iters + 1

        for i in range(0, nvars):
            newx[i] = xbefore[i]

        newf, newx, funevals = best_nearby(delta, newx, fbefore, nvars, f, funevals)
        #
        #  If we made some improvements, pursue that direction.
        #
        keep = True

        while newf < fbefore and keep:

            for i in range(0, nvars):
                #
                #  Arrange the sign of DELTA.
                #
                if newx[i] <= xbefore[i]:
                    delta[i] = - abs(delta[i])
                else:
                    delta[i] = abs(delta[i])
                #
                #  Now, move further in this direction.
                #
                tmp = xbefore[i]
                xbefore[i] = newx[i]
                newx[i] = newx[i] + newx[i] - tmp

            fbefore = newf
            newf, newx, funevals = best_nearby(delta, newx, fbefore, nvars, f, funevals)
            #
            #  If the further (optimistic) move was bad...
            #
            if (fbefore <= newf):
                break
            #
            #  Make sure that the differences between the new and the old points
            #  are due to actual displacements; beware of roundoff errors that
            #  might cause NEWF < FBEFORE.
            #
            keep = False

            for i in range(0, nvars):
                if 0.5 * abs(delta[i]) < abs(newx[i] - xbefore[i]):
                    keep = True
                    break

        if eps <= steplength and fbefore <= newf:
            steplength = steplength * rho
            for i in range(0, nvars):
                delta[i] = delta[i] * rho

    endpt = xbefore.copy()

    return iters, endpt
